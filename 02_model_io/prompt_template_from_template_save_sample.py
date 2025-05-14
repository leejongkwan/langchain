import json
from langchain_core.prompts import PromptTemplate

# 프롬프트 템플릿 생성
prompt = PromptTemplate(
    template="{product}는 어느 회사에서 개발한 제품인가요？",
    input_variables=["product"]
)

# 프롬프트 객체를 딕셔너리로 변환
prompt_dict = {
    "template": prompt.template,
    "input_variables": prompt.input_variables
}

# JSON 파일로 저장
with open("prompt.json", "w", encoding="utf-8") as f:
    json.dump(prompt_dict, f, ensure_ascii=False, indent=2)
