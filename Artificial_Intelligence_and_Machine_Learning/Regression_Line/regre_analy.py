## 회귀 직선 모델
import numpy as np
import matplotlib.pyplot as plt

# 데이터 생성
np.random.seed(1) # 난수 고정
X_n = 16 # 16명 표기용
Hg_C = [170,108,0.2] # 키를 만드는 매개변수 

X = 5 + 25*np.random.rand(X_n) # 나이 생성
T = Hg_C[0] - Hg_C[1] * np.exp(-Hg_C[2]*X) + 4*np.random.rand(X_n) # 키 생성

# 생성한 데이터 출력
print("\n","\n나이 x \n", np.round(X,2)) # 나이 출력
print("\n키 t \n", np.round(T,2)) # 키 출력

# 그래프 그리기
plt.figure(figsize=(4,4))
plt.plot(X, T, marker='o', linestyle='None', markeredgecolor='black', color='cornflowerblue')
plt.xlim(4, 30)
plt.grid(True)
plt.show()










