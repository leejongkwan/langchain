from langchain_core.prompts import PromptTemplate  # 최신 위치에서 import

# PromptTemplate 초기화
prompt = PromptTemplate(
    template="{product}는 어느 회사에서 개발한 제품인가요？",
    input_variables=["product"]
)

# 포맷 적용
print(prompt.format(product="아이폰"))
print(prompt.format(product="갤럭시"))
