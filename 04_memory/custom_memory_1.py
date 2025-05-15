import chainlit as cl
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.messages import BaseMessage

# 1. LLM 초기화
chat = ChatOpenAI(model="gpt-3.5-turbo")

# 2. 메모리 설정 (최근 3턴 기억)
memory = ConversationBufferWindowMemory(
    return_messages=True,
    k=3
)

# 3. Conversation 체인 구성
chain = ConversationChain(
    llm=chat,
    memory=memory
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="✅ 저는 대화의 맥락을 고려해 답변할 수 있는 채팅봇입니다. 메시지를 입력하세요.").send()
    cl.user_session.set("chain", chain)

@cl.on_message
async def on_message(message: cl.Message):
    chain = cl.user_session.get("chain")

    # 4. 저장된 메시지 불러오기 (대화 메모리)
    messages: list[BaseMessage] = chain.memory.chat_memory.messages
    print(f"저장된 메시지 개수: {len(messages)}")
    for msg in messages:
        print(msg.content)

    # 5. 메시지 응답 생성 (invoke 사용)
    response = await chain.ainvoke(message.content)

    await cl.Message(content=response["response"]).send()
