import chainlit as cl

# 채팅이 시작될 때 초기 메시지를 보냄
@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="✅ 준비되었습니다! 메시지를 입력하세요.").send()

# 사용자가 메시지를 보낼 때 실행되는 함수
@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content  # 사용자가 입력한 메시지 텍스트
    print("입력된 메시지: " + user_input)

    # 응답 메시지 전송
    await cl.Message(content="안녕하세요!").send()
