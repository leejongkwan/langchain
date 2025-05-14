from langchain_openai import OpenAI
from langchain_core.runnables import RunnableConfig

# OpenAI instruct 계열 모델 사용
llm = OpenAI(model="gpt-3.5-turbo-instruct")

# 입력 텍스트
prompt = "맛있는 라면을"

# 실행 (stop 조건 포함)
response = llm.invoke(prompt, config=RunnableConfig(stop=["."]))

# 출력
print(response)
