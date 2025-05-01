# 임포트
import numpy as np

# 벡터와 행렬 만들기
a = np.array([1, 2, 3])             # 벡터 1차원
A = np.array([[1, 2], [3, 4]])      # 행렬 2차원

print(a)
print(A)

# 기본 연산
b = np.array([4, 5, 6])

print(a + b)                        # 벡터 덧셈
print(a * 2)                        # 스칼라 곱
print(np.dot(a, b))                 # 내적 (dot product)

# 행렬 연산
B = np.array([[2, 0], [1, 3]])
 
print(np.transpose(B))              # 전치 행렬
print(np.matmul(A, B))              # 행렬 곱
print(np.linalg.inv(B))             # 역행렬

# 선형 시스템 풀기  / Ax = b
A = np.array([[2, 1], [3, 2]])
b = np.array([5, 8])
x = np.linalg.solve(A, b)
print(x)

# 고유값/고유벡터
A = np.array([[4, -2], [1, 1]])
eig_vals, eig_vecs = np.linalg.eig(A)
print("고유값:", eig_vals)
print("고유벡터:\n", eig_vecs)