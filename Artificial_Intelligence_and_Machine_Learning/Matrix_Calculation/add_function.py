### 행렬의 덧셈을 numpy를 쓰지 않고 함수로 계산

def sumMatrix(A, B):
    answer = []
    
    for i in range(len(A)):
        tmp = []
        for j in range(len(A[i])):
            tmp.append(A[i][j] + B[i][j])
        answer.append(tmp)
    return answer

if __name__ == "__main__":
    print(sumMatrix([[1,2],[2,3]],[[3,4],[5,6]]))
    