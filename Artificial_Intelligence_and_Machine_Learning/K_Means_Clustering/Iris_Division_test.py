## K-Means를 이용한 군집화 구현

# 필요한 라이브러리 설치
# pip install scikit-learn
# pip install pyarrow

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pandas as pd # 데이터 프레임으로 변환을 위해 import
import numpy as np # 연산을 위해 import

# 시각화를 위한 패키지 import
import matplotlib.pyplot as plt
import seaborn as sns

# Iris 데이터셋 로드
iris = load_iris()

# 데이터 프레임으로 변환
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# 0.0, 1.0, 2.0으로 표현된 label을 문자열로 매핑
df['target'] = df['target'].map({0:"setosa", 1:"versicolor", 2:"virginica"})  # 'cirginica' 오타 수정

# 슬라이싱을 통해 feature와 label 분리
x_data = df.iloc[:,:-1]
y_data = df.iloc[:,[-1]]

# Seaborn을 사용하여 pairplot 생성
sns.pairplot(df, x_vars=["sepal length (cm)"], y_vars=["sepal width (cm)"], hue="target", height=5)

# 그래프 표시
plt.show()
