from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain_community.retrievers import WikipediaRetriever
from langchain.tools.retriever import create_retriever_tool  # 최신 위치에서 가져오기

# 1. LLM 초기화
chat = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo"
)

# 2. Retriever 정의 (Wikipedia)
retriever = WikipediaRetriever(
    lang="ko",
    doc_content_chars_max=500,
    top_k_results=1
)

# 3. Retriever Tool 생성
retriever_tool = create_retriever_tool(
    retriever=retriever,
    name="WikipediaRetriever",
    description="입력된 단어에 대해 한국어 위키피디아에서 관련 문서를 검색합니다."
)

# 4. Memory 구성
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# 5. Agent 초기화 (대화형 + Retriever tool + Memory)
agent = initialize_agent(
    tools=[retriever_tool],
    llm=chat,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# 6. 실행
result = agent.run("스카치 위스키에 대해 Wikipedia에서 찾아보고 그 개요를 한국어로 정리하세요.")
print(f"1차 실행 결과:\n{result}")

result_2 = agent.run("이전 지시를 다시 한번 실행하세요.")
print(f"\n2차 실행 결과:\n{result_2}")
