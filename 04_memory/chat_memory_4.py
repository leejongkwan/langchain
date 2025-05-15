import os
import chainlit as cl
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_core.messages import HumanMessage

# 1. LLM 초기화
chat = ChatOpenAI(model="gpt-3.5-turbo")

@cl.on_chat_start
async def on_chat_start():
    thread_id = None

    while not thread_id:
        res = await cl.AskUserMessage(
            content="저는 대화의 맥락을 고려해 답변할 수 있는 채팅봇입니다. 스레드 ID를 입력하세요.",
            timeout=600
        ).send()

        if res and res.get("content"):
            thread_id = res["content"]

    # 2. Redis 기반 메시지 기록
    history = RedisChatMessageHistory(
        session_id=thread_id,
        url=os.environ.get("REDIS_URL", "redis://localhost:6379")  # 기본값 설정 가능
    )

    # 3. LangChain 메모리 구성
    memory = ConversationBufferMemory(
        return_messages=True,
        chat_memory=history,
    )

    # 4. Conversation 체인 초기화
    chain = ConversationChain(
        memory=memory,
        llm=chat,
        verbose=True
    )

    # 5. 기존 메시지 불러오기
    messages = memory.chat_memory.messages

    for msg in messages:
        await cl.Message(
            author="User" if isinstance(msg, HumanMessage) else "ChatBot",
            content=msg.content
        ).send()

    # 6. 세션에 저장
    cl.user_session.set("chain", chain)

@cl.on_message
async def on_message(message: cl.Message):
    chain = cl.user_session.get("chain")
    response = await chain.ainvoke(message.content)  # ✅ 비동기 invoke

    await cl.Message(content=response["response"]).send()
