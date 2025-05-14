from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, field_validator  # ✅ field_validator 사용

# OpenAI Chat 모델 초기화
chat = ChatOpenAI(model="gpt-3.5-turbo")

# Pydantic 모델 정의
class Smartphone(BaseModel):
    release_date: str = Field(description="스마트폰 출시일")
    screen_inches: float = Field(description="스마트폰의 화면 크기(인치)")
    os_installed: str = Field(description="스마트폰에 설치된 OS")
    model_name: str = Field(description="스마트폰 모델명")

    @field_validator("screen_inches")  # ✅ 새로운 문법
    @classmethod
    def validate_screen_inches(cls, field):
        if field <= 0:
            raise ValueError("화면 크기는 양수여야 합니다.")
        return field

# OutputParser 초기화
parser = PydanticOutputParser(pydantic_object=Smartphone)

# 프롬프트 메시지
messages = [
    HumanMessage(content="안드로이드 스마트폰 1개를 꼽아주세요"),
    HumanMessage(content=parser.get_format_instructions())
]

# 모델 실행
response = chat.invoke(messages)

# 결과 파싱
parsed_result = parser.parse(response.content)

# 출력
print(f"모델명: {parsed_result.model_name}")
print(f"화면 크기: {parsed_result.screen_inches}인치")
print(f"OS: {parsed_result.os_installed}")
print(f"스마트폰 출시일: {parsed_result.release_date}")
