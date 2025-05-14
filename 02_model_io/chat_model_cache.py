import time
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.globals import set_llm_cache
from langchain_community.cache import InMemoryCache  # ✅ 경고 해결

# 캐시 설정
set_llm_cache(InMemoryCache())

# LLM 모델 정의
chat = ChatOpenAI(model="gpt-3.5-turbo")

# 첫 요청 (캐시 없음)
start = time.time()
result = chat.invoke([HumanMessage(content="안녕하세요!")])
end = time.time()
print(result.content)
print(f"첫 실행 시간: {end - start:.4f}초")

# 두 번째 요청 (캐시 활용됨)
start = time.time()
result = chat.invoke([HumanMessage(content="안녕하세요!")])
end = time.time()
print(result.content)
print(f"두 번째 실행 시간: {end - start:.4f}초")
