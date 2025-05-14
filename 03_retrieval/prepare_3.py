from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# 1. PDF 로드
loader = PyMuPDFLoader("./Azure Data and AI Architect Handbook.pdf")
documents = loader.load()

# 2. 문서 분할 (Spacy → RecursiveCharacterTextSplitter로 대체)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)
splitted_documents = text_splitter.split_documents(documents)

# 3. 임베딩 모델 초기화
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# 4. Chroma 벡터스토어 초기화
vectorstore = Chroma(
    persist_directory="./.data",
    embedding_function=embeddings,
    collection_name="pdf_chunks"  # 명시적으로 컬렉션 지정 권장
)

# 5. 문서 추가
vectorstore.add_documents(splitted_documents)

print("✅ 데이터베이스 생성이 완료되었습니다.")
