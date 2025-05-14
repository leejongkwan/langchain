
from langchain_community.retrievers import WikipediaRetriever

# 최신 WikipediaRetriever 초기화
retriever = WikipediaRetriever(
    lang="ko",  # 한국어 위키피디아
    doc_content_chars_max=100,  # 문서 내용 최대 길이
    top_k_results=1  # 검색 결과 수 제한
)

# 최신 LangChain 스타일: .invoke() 사용
query = "나는 라면을 좋아합니다. 그런데 소주란 무엇인가요?"
documents = retriever.invoke(query)

# 출력
print(f"🔍 문서 개수: {len(documents)}")
for i, doc in enumerate(documents, 1):
    print(f"\n📄 문서 {i} 내용:\n{doc.page_content}")
