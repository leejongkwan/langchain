import random
from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent, Tool
from langchain_community.tools.file_management import WriteFileTool

# 1. LLM 초기화
chat = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo"
)

# 2. 사용자 정의 함수: 특정 최솟값 이상 임의 숫자 생성
def min_limit_random_number(min_number: str) -> str:
    try:
        n = random.randint(int(min_number), 100000)
        return str(n)
    except Exception as e:
        return f"❗ 오류: {e}"

# 3. 도구 목록 정의
tools = [
    # WriteFileTool
    WriteFileTool(root_dir="./"),
    
    # 사용자 정의 Tool
    Tool(
        name="Random",
        description="특정 최솟값 이상의 임의의 숫자를 생성합니다. 입력은 정수 문자열입니다.",
        func=min_limit_random_number
    )
]

# 4. Agent 초기화
agent = initialize_agent(
    tools=tools,
    llm=chat,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 5. 실행
result = agent.run("10 이상의 난수를 생성해 random.txt 파일에 저장하세요.")

# 6. 출력
print(f"실행 결과: {result}")
