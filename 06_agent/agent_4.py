from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, Tool, initialize_agent
from langchain_community.retrievers import WikipediaRetriever
from langchain_community.tools.file_management import WriteFileTool
from langchain.tools.retriever import create_retriever_tool  # 최신 위치에서 가져오기

# 1. LLM 초기화
chat = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo"
)

# 2. 툴 정의
tools = [
    # 파일 저장용 툴
    WriteFileTool(root_dir="./"),

    # Wikipedia Retriever 툴
    create_retriever_tool(
        retriever=WikipediaRetriever(
            lang="ko",
            doc_content_chars_max=500,
            top_k_results=1
        ),
        name="WikipediaRetriever",
        description="입력된 키워드에 대해 한국어 Wikipedia에서 검색 결과를 가져옵니다."
    )
]

# 3. Agent 초기화
agent = initialize_agent(
    tools=tools,
    llm=chat,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 4. 실행
result = agent.run(
    "스카치 위스키에 대해 Wikipedia에서 찾아보고 그 개요를 한국어로 result.txt 파일에 저장하세요."
)

# 5. 출력
print(f"실행 결과: {result}")
