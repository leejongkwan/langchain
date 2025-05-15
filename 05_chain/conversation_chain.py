from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# 1. 언어 모델 초기화
chat = ChatOpenAI(model="gpt-3.5-turbo")

# 2. 메모리 초기화
memory = ConversationBufferMemory(return_messages=True)

# 3. ConversationChain 구성
chain = ConversationChain(
    llm=chat,
    memory=memory,
    verbose=True  # optional: 내부 동작 로깅
)
