import os
import chainlit as cl
from langchain_openai import ChatOpenAI  # 최신 LLM import 경로
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import RedisChatMessageHistory  # ← 최신 위치
from langchain.chains import ConversationChain

# LLM 초기화
chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)

# Redis 기반 대화 기록 관리
history = RedisChatMessageHistory(
    session_id="chat_history",
    url=os.environ.get("REDIS_URL")  # 환경변수에서 Redis URL 가져오기
)

# 메모리 초기화 (Redis 연동)
memory = ConversationBufferMemory(
    return_messages=True,
    chat_memory=history
)

# ConversationChain 구성
chain = ConversationChain(
    llm=chat,
    memory=memory
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="저는 대화의 맥락을 고려해 답변할 수 있는 채팅봇입니다. 메시지를 입력하세요.").send()

@cl.on_message
async def on_message(message: cl.Message):
    # 사용자의 메시지를 chain에 넘겨 응답 받기
    result = await chain.ainvoke(message.content)

    # 응답 출력
