## 벡터 합을 내적으로 나타내기
import numpy as np

# 변수생성
num1 = np.ones(1000) # 1 * 1000 행렬
print(num1, num1.shape)
num2 = np.arange(1, 1001) # 1 * 1000 행렬
print(num2, num2.shape)

# 행렬 곱을 이용하여 내적 구하기
dotOp = num1.dot(num2)
print(dotOp)