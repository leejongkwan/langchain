from langchain_openai import ChatOpenAI
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_core.messages import HumanMessage

# 예시 샘플
examples = [
    {
        "input": "충청도의 계룡산 전라도의 내장산 강원도의 설악산은 모두 국립 공원이다",
        "output": "충청도의 계룡산, 전라도의 내장산, 강원도의 설악산은 모두 국립 공원이다."
    }
]

# 예시 포맷 템플릿
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="입력: {input}\n출력: {output}"
)

# Few-shot Prompt 구성
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="아래 문장부호가 빠진 입력에 문장부호를 추가하세요. 추가할 수 있는 문장부호는 ',', '.'입니다. 다른 문장부호는 추가하지 마세요.",
    suffix="입력: {input_string}\n출력:",
    input_variables=["input_string"]
)

# LLM 초기화 (Chat 기반)
llm = ChatOpenAI(model="gpt-3.5-turbo")

# 프롬프트 구성
formatted_prompt = few_shot_prompt.format(
    input_string="집을 보러 가면 그 집이 내가 원하는 조건에 맞는지 살기에 편한지 망가진 곳은 없는지 확인해야 한다"
)

# 메시지로 래핑하여 전송
messages = [HumanMessage(content=formatted_prompt)]
response = llm.invoke(messages)

# 결과 출력
print("formatted_prompt:\n", formatted_prompt)
print("result:\n", response.content)
