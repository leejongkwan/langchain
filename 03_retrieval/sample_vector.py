from langchain_openai import OpenAIEmbeddings  # 최신 위치
from numpy import dot
from numpy.linalg import norm

# 1. 임베딩 모델 초기화
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# 2. 질의 문장 임베딩
query_vector = embeddings.embed_query("비행 자동차의 최고 속도는?")
print(f"🔍 벡터화된 질문 (앞부분): {query_vector[:5]}")

# 3. 비교할 문서 벡터화
document_1_vector = embeddings.embed_query("비행 자동차의 최고 속도는 시속 150km입니다.")
document_2_vector = embeddings.embed_query("닭고기를 적당히 양념한 후 중불로 굽다가 가끔 뒤집어 주면서 겉은 고소하고 속은 부드럽게 익힌다.")

# 4. 코사인 유사도 계산 함수
def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))

# 5. 유사도 출력
cos_sim_1 = cosine_similarity(query_vector, document_1_vector)
cos_sim_2 = cosine_similarity(query_vector, document_2_vector)

print(f"✅ 문서 1과 질문의 유사도: {cos_sim_1:.4f}")
print(f"✅ 문서 2와 질문의 유사도: {cos_sim_2:.4f}")
