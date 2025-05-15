from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# 1. LLM 초기화
chat = ChatOpenAI(model="gpt-3.5-turbo")

# 2. 프롬프트 템플릿 정의
prompt = PromptTemplate.from_template("{product}는 어느 회사에서 개발한 제품인가요?")

# 3. RunnableSequence (프롬프트 → LLM)
chain = prompt | chat

# 4. 실행
result = chain.invoke({"product": "iPhone"})

# 5. 출력
print(result.content)
