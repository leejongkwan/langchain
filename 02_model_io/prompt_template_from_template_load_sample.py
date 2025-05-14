import json
from langchain_core.prompts import PromptTemplate

# prompt.json 파일 불러오기
with open("prompt.json", "r", encoding="utf-8") as f:
    prompt_data = json.load(f)

# PromptTemplate 구성
loaded_prompt = PromptTemplate(**prompt_data)

# 프롬프트 적용
print(loaded_prompt.format(product="iPhone"))
