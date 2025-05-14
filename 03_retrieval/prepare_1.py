from langchain_community.document_loaders import PyMuPDFLoader

# PDF 파일 로드
loader = PyMuPDFLoader("./Azure Data and AI Architect Handbook.pdf")
documents = loader.load()

# 문서 정보 출력
print(f"문서 개수: {len(documents)}")
print(f"첫 번째 문서의 내용: {documents[0].page_content}")
print(f"첫 번째 문서의 메타데이터: {documents[0].metadata}")
