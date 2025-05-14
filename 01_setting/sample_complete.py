import openai
import os

# 환경변수에서 API 키 가져오기
openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key is None:
    raise ValueError("OPENAI_API_KEY 환경변수가 설정되어 있지 않습니다.")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, world!"}],
    max_tokens=50
)

print(response['choices'][0]['message']['content'])