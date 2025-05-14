from langchain_community.retrievers import WikipediaRetriever

# 1. WikipediaRetriever 초기화 (한국어 설정)
retriever = WikipediaRetriever(
    lang="ko",  # 한국어 위키백과에서 검색
)

# 2. 질문 정의
query = "대형 언어 모델"

# 3. 최신 방식: invoke()로 검색
documents = retriever.invoke(query)

# 4. 결과 출력
print(f"🔍 검색 결과: {len(documents)}건")

for document in documents:
    print("---------------검색한 메타데이터---------------")
    print(document.metadata)

    print("---------------검색한 텍스트---------------")
    print(document.page_content[:100])  # 첫 100자만 표시
