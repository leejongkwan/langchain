import requests
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# 1. LLM 초기화
chat = ChatOpenAI(model="gpt-3.5-turbo")

# 2. 프롬프트 템플릿 정의
prompt = PromptTemplate.from_template(
    """아래 문장을 바탕으로 질문에 답해 주세요.

문장: {requests_result}
질문: {query}"""
)

# 3. 프롬프트 → LLM 체인 구성
chain = prompt | chat

# 4. 외부 API 요청
response = requests.get("https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json")
json_data = response.json()

# 5. 필요한 필드 추출 (예: 헤드라인 텍스트)
requests_result = json_data.get("text", "정보를 불러올 수 없습니다.")

# 6. LLM에 전달
result = chain.invoke({
    "query": "도쿄의 날씨를 알려주세요",
    "requests_result": requests_result
})

# 7. 응답 출력
print(result.content)
