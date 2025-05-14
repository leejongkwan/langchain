from datetime import datetime
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage

# 날짜 파싱 함수 정의
def parse_datetime_from_text(text: str) -> datetime:
    for fmt in ("%Y-%m-%d", "%Y.%m.%d", "%Y/%m/%d", "%Y년 %m월 %d일"):
        try:
            return datetime.strptime(text.strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"날짜 형식을 인식할 수 없습니다: {text}")

# 모델 초기화
chat = ChatOpenAI(model="gpt-3.5-turbo")

# 프롬프트 템플릿 정의
prompt = PromptTemplate.from_template("{product}의 출시일을 yyyy-mm-dd 형식으로 알려주세요")

# 프롬프트 적용 및 실행
messages = [
    HumanMessage(content=prompt.format(product="iPhone8")),
]
response = chat.invoke(messages)

# 결과 파싱
output_text = response.content
print(f"모델 출력: {output_text}")

try:
    output_datetime = parse_datetime_from_text(output_text)
    print(f"파싱된 날짜: {output_datetime}")
except Exception as e:
    print(f"파싱 실패: {e}")
