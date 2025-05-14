from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# 스트리밍 출력 핸들러 정의
streaming_handler = StreamingStdOutCallbackHandler()

# ChatOpenAI 인스턴스 생성 (스트리밍 활성화)
chat = ChatOpenAI(
    streaming=True,
    callbacks=[streaming_handler],
    model="gpt-3.5-turbo"  # 또는 "gpt-4"
)

# 메시지 전송 (스트리밍 출력)
resp = chat.invoke([
    HumanMessage(content="맛있는 스테이크 굽는 법을 알려주세요")
])
