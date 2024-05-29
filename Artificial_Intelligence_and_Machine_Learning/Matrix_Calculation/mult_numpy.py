### 행렬의 곱샘을 numpy를 써서 함수로 계산

import numpy as np

if __name__ == "__main__":
    
    ## 행렬 선언
    A = np.array([[2,3],[4,1]])
    B = np.array([[5,7],[6,8]])
    
    ## 행렬의 인덱스 곱
    print("\nA * B =\n",A * B)
    print()
    
    ## 행렬 곱
    print("\nA dot B =\n", np.dot(A,B))
    print()
    
