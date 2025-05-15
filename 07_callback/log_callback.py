from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI


# 커스텀 콜백 핸들러 정의
class LogCallbackHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        print("✅ Chat model 실행 시작...")
        print(f"📨 입력 메시지: {messages}")

    def on_chain_start(self, serialized, inputs, **kwargs):
        print("🔗 Chain 실행 시작...")
        print(f"📥 입력: {inputs}")


# LLM 초기화 (콜백 핸들러 포함)
chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    callbacks=[LogCallbackHandler()]
)

# LLM 실행
result = chat.invoke([
    HumanMessage(content="안녕하세요!")
])

# 결과 출력
print("💬 응답:", result.content)
