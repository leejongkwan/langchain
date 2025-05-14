from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_core.documents import Document

# 1. LLM 및 임베딩 모델 초기화
chat = ChatOpenAI(model="gpt-3.5-turbo")
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# 2. Chroma 로드
vectorstore = Chroma(
    persist_directory="./.data",
    embedding_function=embeddings,
    collection_name="pdf_chunks"  # 삽입 시 사용한 collection_name과 일치해야 함
)

# 3. Retriever 변환
retriever = vectorstore.as_retriever()

# 4. RetrievalQA 체인 구성
qa_chain = RetrievalQA.from_llm(
    llm=chat,
    retriever=retriever,
    return_source_documents=True
)

# 5. 질의 실행
query = "비행 자동차의 최고 속도를 알려주세요"
result = qa_chain.invoke(query)

# 6. 결과 출력
print("🧠 답변:")
print(result["result"])

print("\n📄 참조 문서:")
for doc in result["source_documents"]:
    print(f"- {doc.metadata.get('source', '알 수 없음')}")
    print(doc.page_content[:300], "...\n")
