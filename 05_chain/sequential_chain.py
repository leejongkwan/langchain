from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

# 1. LLM 초기화
chat = ChatOpenAI(model="gpt-3.5-turbo")

# 2. 기사 작성 프롬프트 + 체인
write_prompt = PromptTemplate.from_template("{input}에 관한 기사를 써주세요.")
write_chain = write_prompt | chat

# 3. 번역 프롬프트 + 체인
translate_prompt = PromptTemplate.from_template("다음 문장을 영어로 번역해 주세요.\n{input}")
translate_chain = translate_prompt | chat

# 4. SimpleSequentialChain 대체: 체인 연결
sequential_chain = RunnableLambda(
    lambda input_text: write_chain.invoke({"input": input_text}).content
).bind() | RunnableLambda(
    lambda article: translate_chain.invoke({"input": article}).content
)

# 5. 실행
result = sequential_chain.invoke("일렉트릭 기타 선택 방법")

# 6. 출력
print(result)
