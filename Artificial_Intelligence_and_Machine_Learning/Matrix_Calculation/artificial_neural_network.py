### 행렬의 곱을 응용하여 신경망에 적용
# A -(w)-> Y

import numpy as np

x = np.array([5,10])
w = np.array([[1,3,5],[2,4,6]])
Y = np.dot(x,w)

print(w,'\n',Y)