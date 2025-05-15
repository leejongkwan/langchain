import chainlit as cl
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory
from langchain_core.messages import BaseMessage

# 1. LLM 초기화
chat = ChatOpenAI(model="gpt-3.5-turbo")

# 2. 요약 기반 메모리 구성
memory = ConversationSummaryMemory(
    llm=chat,
    return_messages=True
)

# 3. 대화 체인 구성
chain = ConversationChain(
    llm=chat,
    memory=memory
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="✅ 저는 대화의 맥락을 요약해 기억하는 채팅봇입니다. 메시지를 입력해 주세요.").send()
    cl.user_session.set("chain", chain)

@cl.on_message
async def on_message(message: cl.Message):
    chain = cl.user_session.get("chain")

    # 4. 저장된 요약 메시지 출력
    messages: list[BaseMessage] = chain.memory.chat_memory.messages
    print(f"저장된 메시지 개수: {len(messages)}")
    for m in messages:
        print(m.content)

    # 5. 사용자 메시지에 대한 응답 생성
    response = await chain.ainvoke(message.content)

    await cl.Message(content=response["response"]).send()
