### 행렬의 곱셉을 numpy를 쓰지 않고 함수로 계산

def matrixmult(A, B):
    n = len(A)
    c = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += A[i][k]*B[k][j]
    return c

if __name__ == "__main__":
    A = [[2,3],[4,1]]
    B = [[5,7],[6,8]]
    C = matrixmult(A, B)
    print('A = ',A,'\nB = ',B,'\nC = ',C)
    