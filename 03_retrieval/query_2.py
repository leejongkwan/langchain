from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage

# 1. 임베딩 및 DB 초기화
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

vectorstore = Chroma(
    persist_directory="./.data",
    embedding_function=embeddings,
    collection_name="pdf_chunks"  # 삽입 시 사용한 이름과 동일하게
)

# 2. 질의 정의 및 유사도 검색
query = "비행 자동차의 최고 속도는?"
documents = vectorstore.similarity_search(query)

# 3. 검색된 문서 문자열로 정리
documents_string = "\n---------------------------\n".join(
    doc.page_content for doc in documents
)

# 4. 프롬프트 템플릿 구성
prompt = PromptTemplate(
    template="""문장을 바탕으로 질문에 답하세요.

문장: 
{document}

질문: {query}
""",
    input_variables=["document", "query"]
)

# 5. Chat 모델 생성
chat = ChatOpenAI(model="gpt-3.5-turbo")

# 6. LLM 호출
response = chat.invoke([
    HumanMessage(content=prompt.format(document=documents_string, query=query))
])

# 7. 결과 출력
print(response.content)
