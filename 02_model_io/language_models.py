from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(  #← 클라이언트를 만들고 chat에 저장
    model="gpt-3.5-turbo",  #← 호출할 모델 지정
)


result = chat.invoke([HumanMessage(content="안녕하세요!")])
print(result.content)
