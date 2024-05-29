## K-Means를 이용한 군집화 구현

from sklearn import datasets
from matplotlib import pyplot as plt
from copy import deepcopy
import numpy as np 
from sklearn.cluster import KMeans

# 붓꽃 데이터 가져오기
iris = datasets.load_iris()
samples = iris.data
x = samples[:,0]
y = samples[:,1]

plt.figure(1) # 붓꽃 데이터 시각화
plt.scatter(x, y, alpha=0.5)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
# plt.show()


## 임의의 3개의 중심 위치 배정
k = 3
# 랜덤으로 x, y 좌표 3개 생성
# np.random.uniform은 주어진 최소, 최댓값 사이에서 k개만큼 실수 난수를 생성
centroids_x = np.random.uniform(min(x), max(x), k)
centroids_y = np.random.uniform(min(y), max(y), k)
centroids = list(zip(centroids_x, centroids_y))
plt.figure(2)
plt.scatter(x, y, alpha=0.5)
plt.scatter(centroids_x, centroids_y, marker='D', s=150) # centroid는 주황색 다이아몬드 표시
# plt.show()


## 새로운 중심 위치로 데이터 배정
def distance(a, b):
    return sum([(el_a - el_b)**2 for el_a, el_b in list(zip(a, b))]) ** 0.5
labels = np.zeros(len(samples)) # 각 데이터 위치를 그룹화할 labels 생성(0,1,2)
sepal_length_width = np.array(list(zip(x, y)))

for i in range(len(samples)): # 각 데이터를 순회하면서 centroids와의 거리 측정
    distances = np.zeros(k) # 초기거리는 0으로 초기화
    for j in range(k):
        distances[j] = distance(sepal_length_width[i], centroids[j])
    cluster = np.argmin(distances) # np.argmin은 가장 작은 값의 index 변환
    labels[i] = cluster
plt.figure(3)
plt.scatter(x, y, c=labels, alpha=0.5)
plt.scatter(centroids_x, centroids_y, c='red', marker='D', s=150) # centroid는 빨간색 다이아몬드 표시
# plt.show()


## 중심 위치 갱신
centroids_old = np.array(deepcopy(centroids))
centroids_new = np.array(deepcopy(centroids))

for i in range(k): 
    # 각 그룹에 속한 데이터만 골라 points에 저장한다
    points = [sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i]
    # points의 각 feature, 즉 각 좌표의 평균 지점을 centroid로 지정 
    centroids_new[i] = np.mean(points, axis=0)

plt.figure(4)
plt.scatter(x, y, c=labels, alpha=0.5)
plt.scatter(centroids_old[:,0], centroids_old[:,1], c='blue', marker='D', s=150) # centroid는 파란색 다이아몬드 표시
plt.scatter(centroids_new[:,0], centroids_new[:,1], c='red', marker='s', s=150) # centroid는 빨간색 사각형 표시
# plt.show()


## 중심점의 위치가 최적이 되도록 반복
centroids_old = np.zeros(np.array(centroids_new).shape)
labels = np.zeros(len(samples))
error = np.zeros(k) # error 초기화

# 초기 에러 계산
for i in range(k):
    error[i] = distance(centroids_old[i], centroids_new[i])  

# error가 0에 수렴할 때까지 2~3단계 반복
while(error.all() != 0): 
    # STEP 2 : 가까운 centroids에 데이터를 할당
    for i in range(len(samples)):
        distances = np.zeros(k) # 초기거리는 모두 0으로 초기화
        for j in range(k):
            distances[j] = distance(sepal_length_width[i], centroids_new[j])
        cluster = np.argmin(distances) # np.argmin은 가장 작은 값의 index를 반환
        labels[i] = cluster
    # STEP 3 : centroids 업데이트
    centroids_old = deepcopy(centroids_new)
    for i in range(k):
        # 각 그룹에 속한 데이터들만 골라 points에 저장
        points = [ sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i ]
        # points의 각 features, 각 좌표의 평균 지점을 centroid로 지정
        centroids_new[i] = np.mean(points, axis=0)
    # 새롭게 centroids를 업데이트 했으니 error를 다시 계산
    for i in range(k):
        error[i] = distance(centroids_old[i], centroids_new[i])

colors = ['r', 'g', 'b']
plt.figure(5)
for i in range(k):
    points = np.array([sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i])
    plt.scatter(points[:,0], points[:,1], c=colors[i], alpha=0.5)
    
plt.scatter(centroids_new[:,0], centroids_new[:,1], marker='D', s=150) # centroid는 파란색 다이아몬드 표시    
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
# plt.show()


## 소스코드 및 결과  kmeans 알고리즘 : 군집화
# 3개의 그룹으로 나누는 K-Means 모델 생성
model = KMeans(n_clusters = 3)
model.fit(samples)
labels = model.predict(samples)

# 클러스터링 결과 시각화
x = samples[:,0]
y = samples[:,1]

plt.figure(6)
plt.scatter(x, y, c=labels, alpha=0.5)  
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()

