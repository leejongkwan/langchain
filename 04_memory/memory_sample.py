from langchain.memory import ConversationBufferMemory

# 1. 메모리 초기화
memory = ConversationBufferMemory(
    return_messages=True
)

# 2. 대화 기록 저장
memory.save_context(
    {"input": "안녕하세요!"},
    {"output": "안녕하세요! 잘 지내고 계신가요? 궁금한 점이 있으면 알려 주세요. 어떻게 도와드릴까요?"}
)

memory.save_context(
    {"input": "오늘 날씨가 좋네요"},
    {"output": "저는 AI이기 때문에 실제 날씨를 느낄 수는 없지만, 날씨가 좋은 날은 외출이나 활동을 즐기기에 좋은 날입니다!"}
)

# 3. 메모리 내용 출력
variables = memory.load_memory_variables({})
print("📚 저장된 메모리:")
print(variables["history"])
