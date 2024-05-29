## 로지스틱 회귀를 이용한 생존분석 구현

from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

passengers = pd.read_csv('train.csv') # 데이터 불러오기
print(passengers.shape) 
print(passengers.head()) #컬럼확인

# 성별 문자 -> 숫자로 변환
passengers['Sex'] = passengers['Sex'].map({'female':1,'male':0})
passengers['Age'].fillna(value=passengers['Age'].mean(), inplace=True)

# 좌석 등급 필드 추가
passengers['FirstClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 1 else 0)
passengers['SecondClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 2 else 0)

# 특징 분리
features = passengers[['Sex', 'Age', 'FirstClass', 'SecondClass']] # 독립변수 (입력)
survival = passengers['Survived'] # 종속변수 (출력)

# 학습데이터와 테스트 데이터 분리
train_features, test_features, train_labels, test_labels = train_test_split(features, survival)

# 정규화
scaler = StandardScaler()
train_features = scaler.fit_transform(train_features)
test_features = scaler.transform(test_features)

# 모델생성
model = LogisticRegression(random_state = 0, solver='lbfgs')
model.fit(train_features, train_labels)

# 학습데이터 정확도 출력
print(model.score(train_features, train_labels))

# 테스트 데이터 정확도 출력
print(model.score(test_features, test_labels))

# 특징의 계수 확인 : 어떤 feature가 생존에 큰 영향을 주는지 알아보기
print(model.coef_)

# 새로운 데이터로 예측하기

Hong = np.array([0.0, 20.0, 1.0, 0.0])
Park = np.array([1.0, 17.0, 0.0, 0.0])
Kim = np.array([0.0, 40.0, 1.0, 0.0])

sample_passengers = np.array([Hong, Park, Kim])
sample_passengers = scaler.transform(sample_passengers)

print(model.predict(sample_passengers))
print(model.predict_proba(sample_passengers))







