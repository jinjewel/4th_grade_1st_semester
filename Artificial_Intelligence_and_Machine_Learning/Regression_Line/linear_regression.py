## 선형회귀를 이용한 키 예측 구현

import matplotlib.pylab as plt
from sklearn import linear_model

reg = linear_model.LinearRegression()

x = [[174],[152],[138],[128],[186]]
y = [71,55,46,38,88]
reg.fit(x, y) # 학습

print(reg.predict([[165]]))

# 학습 데이터와 y값을 산포도로 그린다.
plt.scatter(x, y, color='black')

# 학습 데이터를 입력으로 하여 예측값을 계산한다.
y_pred = reg.predict(x)

# 학습데이터와 예측값으로 선그래프로 그린다.
# 계산된 기울기와 y절편을 가지는 직선이 그려진다.
plt.plot(x, y_pred, color='blue', linewidth=3)
plt.show()