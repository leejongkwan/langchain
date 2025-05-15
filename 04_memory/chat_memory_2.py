import chainlit as cl
from langchain_openai import ChatOpenAI  # 최신 구조
from langchain.memory import ConversationBufferMemory  # 여전히 본체에 있음
from langchain.chains import ConversationChain

# LLM 초기화
chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)

# 대화 메모리 초기화
memory = ConversationBufferMemory(return_messages=True)

# 대화 체인 구성
chain = ConversationChain(
    llm=chat,
    memory=memory
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="저는 대화의 맥락을 고려해 답변할 수 있는 채팅봇입니다. 메시지를 입력하세요.").send()

@cl.on_message
async def on_message(message: cl.Message):
    # 최신 방식은 await + ainvoke 사용
    result = await chain.ainvoke(message.content)

    await cl.Message(content=result["response"]).send()
