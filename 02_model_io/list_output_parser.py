from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.messages import HumanMessage

# 출력 파서 초기화
output_parser = CommaSeparatedListOutputParser()

# OpenAI 모델 초기화
chat = ChatOpenAI(model="gpt-3.5-turbo")

# 메시지 구성
messages = [
    HumanMessage(content="애플이 개발한 대표적인 제품 3개를 알려주세요"),
    HumanMessage(content=output_parser.get_format_instructions()),
]

# 모델 응답 받기
response = chat.invoke(messages)

# 결과 파싱
output = output_parser.parse(response.content)

# 출력
for item in output:
    print("대표 상품 => " + item)
