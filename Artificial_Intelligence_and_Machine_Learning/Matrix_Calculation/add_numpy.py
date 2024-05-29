### 행렬의 덧셈을 numpy를 써서 함수로 계산

import numpy as np

def sumMatrix(A, B):
    
    A = np.matrix(A)
    B = np.matrix(B)
    answer = A + B
    
    return answer

if __name__ == "__main__":
    print(sumMatrix([[1,2],[2,3]],[[3,4],[5,6]]))
    