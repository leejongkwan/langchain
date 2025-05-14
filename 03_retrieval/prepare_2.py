from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter  # 대체 splitter 사용

# PDF 문서 로드
loader = PyMuPDFLoader("./Azure Data and AI Architect Handbook.pdf")
documents = loader.load()

# RecursiveCharacterTextSplitter 초기화
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,       # 분할 크기
    chunk_overlap=50,     # 중첩 크기 (문맥 유지용)
    separators=["\n\n", "\n", ".", " ", ""]  # 분할 기준 우선순위
)

# 문서 분할
splitted_documents = text_splitter.split_documents(documents)

# 결과 출력
print(f"분할 전 문서 개수: {len(documents)}")
print(f"분할 후 문서 개수: {len(splitted_documents)}")
