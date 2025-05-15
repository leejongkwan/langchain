from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# 1. LLM 초기화
chat = ChatOpenAI(model="gpt-3.5-turbo")

# 2. 메시지 입력
messages = [HumanMessage(content="계란찜을 만드는 재료를 알려주세요")]

# 3. 최신 실행 방식: invoke()
response = chat.invoke(messages)

# 4. 응답 출력
print(response.content)
