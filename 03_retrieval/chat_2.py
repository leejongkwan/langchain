import chainlit as cl
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage

# 임베딩 모델 정의
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# Chat 모델 정의
chat = ChatOpenAI(model="gpt-3.5-turbo")

# 프롬프트 템플릿 정의
prompt = PromptTemplate(
    template="""문장을 바탕으로 질문에 답하세요.

문장:
{document}

질문: {query}
""",
    input_variables=["document", "query"]
)

# Chroma DB 로딩
database = Chroma(
    persist_directory="./.data",
    collection_name="my_docs",  # 필요 시 지정
    embedding_function=embeddings
)

# 채팅 시작 시 초기 메시지 전송
@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="✅ 준비되었습니다! 질문을 입력해주세요.").send()

# 메시지 처리 핸들러
@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content
    print("입력된 메시지:", user_input)

    # 유사 문서 검색
    documents = database.similarity_search(user_input)

    # 문서 문자열 합치기
    documents_string = "\n---------------------------\n".join(
        doc.page_content for doc in documents
    )

    # LLM 호출
    response = chat.invoke([
        HumanMessage(content=prompt.format(document=documents_string, query=user_input))
    ])

    # 응답 전송
    await cl.Message(content=response.content).send()
