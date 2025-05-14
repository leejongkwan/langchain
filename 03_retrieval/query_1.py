from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# 1. 임베딩 모델 초기화
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# 2. Chroma 벡터 DB 초기화 (persist_directory 지정된 경우 기존 데이터 로드됨)
vectorstore = Chroma(
    persist_directory="./.data",
    embedding_function=embeddings,
    collection_name="pdf_chunks"  # 기존 삽입 시 사용한 collection_name
)

# 3. 질의 기반 유사도 검색
query = "비행 자동차의 최고 속도는?"
documents = vectorstore.similarity_search(query)

# 4. 결과 출력
print(f"문서 개수: {len(documents)}")

for i, document in enumerate(documents, start=1):
    print(f"\n📄 문서 {i} 내용:\n{document.page_content}")
