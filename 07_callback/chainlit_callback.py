import chainlit as cl
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import AgentType, initialize_agent

chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

tools = load_tools(["serpapi"], llm=chat, allow_dangerous_tools=True)

agent = initialize_agent(
    tools=tools,
    llm=chat,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="✅ Agent가 초기화되었습니다. 메시지를 입력해 주세요.").send()

@cl.on_message
async def on_message(message: cl.Message):
    result = agent.run(message.content)
    await cl.Message(content=result).send()
