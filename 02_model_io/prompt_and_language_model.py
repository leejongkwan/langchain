from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage

# ChatOpenAI 클라이언트 생성
chat = ChatOpenAI(model="gpt-3.5-turbo")

# PromptTemplate 정의
prompt = PromptTemplate(
    template="{product}는 어느 회사에서 개발한 제품인가요?",
    input_variables=["product"]
)

# 프롬프트에 변수 적용
formatted_prompt = prompt.format(product="아이폰")

# 메시지 구성 및 실행
response = chat.invoke([
    HumanMessage(content=formatted_prompt)
])

# 출력
print(response.content)
