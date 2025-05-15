import chainlit as cl
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory  # ← 수정된 경로
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)

memory = ConversationBufferMemory(return_messages=True)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="저는 대화의 맥락을 고려해 답변할 수 있는 채팅봇입니다. 메시지를 입력하세요.").send()

@cl.on_message
async def on_message(message: cl.Message):
    memory_result = memory.load_memory_variables({})
    messages = memory_result.get('history', [])
    
    messages.append(HumanMessage(content=message.content))

    response = await chat.ainvoke(messages)

    memory.save_context(
        inputs={"input": message.content},
        outputs={"output": response.content}
    )

    await cl.Message(content=response.content).send()
