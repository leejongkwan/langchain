from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain_community.agent_toolkits.load_tools import load_tools  # ← 최신 위치

# 1. LLM 설정
chat = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo"
)

# 2. 위험 도구 로드 시 명시적으로 허용
tools = load_tools(
    ["requests_all"],
    llm=chat,
    allow_dangerous_tools=True  # ← 필수!
)

# 3. 에이전트 초기화
agent = initialize_agent(
    tools=tools,
    llm=chat,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 4. 실행
result = agent.run("""
아래 URL에 접속해 도쿄의 날씨를 확인하고 한국어로 요약해 주세요.
https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json
""")

print("실행 결과:", result)
