# 기본조건
# 같은 행은 퀸을 놓지 않는다.

# 유망 조건
# 같은 열, 같은 대각선에 놓이는지를 확인
# 같은 열 체크
# col[i] : i번째 행(row)에서 퀸이 놓여있는 열의 위치
# col[k] : k번째 행(row)에서 퀸이 놓여있는 열의 위치
# col[i] == col[k] 라면 같은 열이므로 조건 x
# 같은 대각선 체크
# 왼쪽에서 위협하는 열에서의 차이는 행에서의 차이와 같다
# col[i] - col[k] == i - k
# 오른쪽에서 위협하는 열에서의 차이는 행에서의 차이와 같다
# col[k] - col[i] == k - i
# col[i]와 col[k]의 절대값으로 대각선 위협 판단

import sys

N = int(sys.stdin.readline())

count = 0
col = [0] * (N + 1)

def promising(i, col):
    k = 1
    flag = True
    while(k < i and flag):
        if (col[i] == col[k]) or abs(col[i] - col[k]) == (i - k) :
            flag = False
        k += 1
    return flag

def n_queens(i, col):
    global count
    n = len(col) - 1
    if (promising(i, col)):
        if(i == n):            
            count += 1            
        else:
            for j in range(1, n+1):
                col[i + 1] = j
                n_queens(i + 1, col) 

n_queens(0, col)
print(count)

