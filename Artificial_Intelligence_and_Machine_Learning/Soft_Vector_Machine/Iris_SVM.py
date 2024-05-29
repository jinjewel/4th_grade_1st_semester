## SVM을 이용한 분류 구현

## 붓꽃 데이터 가져오기
import numpy as np 
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import mglearn

# 시각화를 위해 sepal length와 sepal width만 사용
iris = load_iris() # 붓꽃 데이터 불러오기
x = iris.data[:, [0,1]] #colume 0과 1만 사용함.
y = iris.target

# 데이터 분리 : 120개 훈련데이터 30개 테스트 데이터
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

# 데이터 확인
print(X_train)
print(y_train)


## 데이터 정규화
print("꽃받침 길이 값의 범위 : ", "[", min(X_train[:,0]), ",", max(X_train[:,0]),"]")
print("꽃받침 길이 값의 범위 : ", "[", min(X_train[:,1]), ",", max(X_train[:,1]),"]")

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

print("표준화된 꽃받침 길이 값의 범위 : ", "[", min(X_train_std[:,0]), ",", max(X_train_std[:,0]),"]")
print("표준화된 꽃받침 길이 값의 범위 : ", "[", min(X_train_std[:,1]), ",", max(X_train_std[:,1]),"]")


## 학습 및 테스트
svm_model = SVC(kernel='linear', C=8, gamma=0.1)
svm_model.fit(X_train_std, y_train) # SVM 분류 모델 훈련

y_pred = svm_model.predict(X_test_std) # 성능 측정

print("예측된 라벨:", y_pred)
print("ground-truth 라벨:", y_test)
print("prediction accuracy: {:.2f}".format(np.mean(y_pred == y_test)))


## 시각화
plt.figure(figsize=[9,7])
mglearn.plots.plot_2d_classification(svm_model, X_train_std, alpha=0.1)
mglearn.discrete_scatter(X_train_std[:, 0], X_train_std[:, 1], y_train)
plt.legend(iris.target_names)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()

