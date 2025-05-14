from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_community.retrievers import WikipediaRetriever

# 1. LLM 초기화 (GPT-3.5-Turbo 기본)
chat = ChatOpenAI(model="gpt-3.5-turbo")

# 2. Wikipedia 리트리버 설정
retriever = WikipediaRetriever(
    lang="ko",
    doc_content_chars_max=500,
    top_k_results=2
)

# 3. RetrievalQA 체인 구성
qa_chain = RetrievalQA.from_llm(
    llm=chat,
    retriever=retriever,
    return_source_documents=True
)

# 4. 질문 실행
query = "소주란?"
result = qa_chain.invoke(query)  # ✅ 최신 방식: invoke

# 5. 결과 및 출처 출력
source_documents = result["source_documents"]

print(f"🔍 검색 결과: {len(source_documents)}건")
for document in source_documents:
    print("---------------검색한 메타데이터---------------")
    print(document.metadata)
    print("---------------검색한 텍스트---------------")
    print(document.page_content[:100])

print("---------------응답---------------")
print(result["result"])
