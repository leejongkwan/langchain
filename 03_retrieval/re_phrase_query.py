from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.retrievers import WikipediaRetriever

# 1. 모델 및 프롬프트 정의
llm = ChatOpenAI(temperature=0)
prompt = PromptTemplate(
    input_variables=["question"],
    template="아래 질문에서 Wikipedia에서 검색할 키워드를 추출해 주세요.\n질문: {question}"
)

# 2. 직접 키워드 추출 (prompt | llm)
keyword_extractor = prompt | llm

query = "나는 라면을 좋아합니다. 그런데 소주란 무엇인가요?"
keyword_result = keyword_extractor.invoke({"question": query})

# 3. 추출된 키워드 확인
rephrased_query = keyword_result.content if hasattr(keyword_result, "content") else str(keyword_result)

# 4. Wikipedia 검색
retriever = WikipediaRetriever(lang="ko", doc_content_chars_max=500)
documents = retriever.invoke(rephrased_query)

# 5. 결과 출력
print(f"🔍 문서 수: {len(documents)}")
for i, doc in enumerate(documents, 1):
    print(f"\n📄 문서 {i}:\n{doc.page_content[:300]}...\n")
