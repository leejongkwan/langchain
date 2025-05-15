from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.tools.file_management import WriteFileTool

# 1. LLM 초기화
chat = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo"
)

# 2. 도구 로딩 (요청/검색용)
tools = load_tools(
    ["requests_get", "serpapi"],
    llm=chat,
    allow_dangerous_tools=True  # serpapi나 requests가 위험할 수 있으므로 명시적으로 허용
)

# 3. 파일 쓰기 도구 추가
tools.append(
    WriteFileTool(root_dir="./")
)

# 4. Agent 초기화 (Structured Chat 방식)
agent = initialize_agent(
    tools=tools,
    llm=chat,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 5. 실행 (파일 저장 명령 포함)
result = agent.run("경주시의 특산물을 검색해서 result.txt 파일에 한국어로 저장하세요.")

# 6. 출력
print(f"실행 결과: {result}")
