import os
import chainlit as cl
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Define embedding and chat models
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
chat = ChatOpenAI(model="gpt-3.5-turbo")

# Define prompt template
prompt = PromptTemplate(
    template="""문장을 기반으로 질문에 답하세요.

문장: 
{document}

질문: {query}
""",
    input_variables=["document", "query"]
)



text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)


@cl.on_chat_start
async def on_chat_start():
    files = None

    while files is None:
        files = await cl.AskFileMessage(
            max_size_mb=20,
            content="PDF를 선택해 주세요",
            accept=["application/pdf"],
            raise_on_timeout=False,
        ).send()

    file = files[0]
    # 최신 Chainlit: content가 아닌 path 사용
    file_path = file.path  # ← 이 경로를 그대로 PyMuPDFLoader에 전달

    documents = PyMuPDFLoader(file_path).load()

    splitted_documents = text_splitter.split_documents(documents)

    # Initialize in-memory Chroma DB (no persistence)
    vectorstore = Chroma(
        collection_name="temp_collection",
        embedding_function=embeddings
    )
    vectorstore.add_documents(splitted_documents)

    # Store in session
    cl.user_session.set("vectorstore", vectorstore)

    await cl.Message(content=f"`{file.name}` 로딩이 완료되었습니다. 질문을 입력하세요.").send()

@cl.on_message
async def on_message(message: cl.Message):
    query = message.content
    print("입력된 메시지:", query)

    vectorstore = cl.user_session.get("vectorstore")
    documents = vectorstore.similarity_search(query)

    documents_string = "\n---------------------------\n".join(
        doc.page_content for doc in documents
    )

    response = chat.invoke([
        HumanMessage(content=prompt.format(document=documents_string, query=query))
    ])

    await cl.Message(content=response.content).send()
