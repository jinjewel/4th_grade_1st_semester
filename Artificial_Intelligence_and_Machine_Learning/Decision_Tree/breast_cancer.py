## 의사결정트리를 이용한 유방함 판독 구현

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
import pydot

# 샘플 데이터 로드(유방암 데이터 세트)
cancer = load_breast_cancer()

# 훈련, 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)

# 의사결정 트리 선언
dTreeAll = DecisionTreeClassifier(random_state=0) # 난수시드 설정

# 훈력 (모든 리프 노드 사용)
dTreeAll.fit(X_train, y_train)

# 점수 출력
print("Trian set score1 : {:.2f}".format(dTreeAll.score(X_train, y_train)))
print("Trian set score1 : {:.2f}".format(dTreeAll.score(X_test, y_test)))

# 가지치기
# 트리 깊이 제한
dTreeLimit = DecisionTreeClassifier(max_depth=3, random_state=0)

# 춘련 (다말리프노드 깊이 제한)
dTreeLimit.fit(X_train, y_train)

# 점수 출력
print("Trian set score2 : {:.2f}".format(dTreeLimit.score(X_train, y_train)))
print("Trian set score2 : {:.2f}".format(dTreeLimit.score(X_test, y_test)))

export_graphviz(dTreeLimit, out_file="dicisionTree1.dot", 
                class_names=["malignant","benign"],
                feature_names=cancer.feature_names, 
                impurity=False, filled=True)


# 인고딩 중요
(graph,) = pydot.graph_from_dot_file('dicisionTree1.dot', encoding='utf8')

# Dot 파일을 Png 이미지로 저장
graph.write_png('dicisionTree.png')














