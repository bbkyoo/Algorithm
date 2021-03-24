import sys
input = sys.stdin.readline

def find_squre(s): # 이 부분이 제일 중요
    for i in range(n-s+1):
        for j in range(m-s+1):
            if matrix[i][j] == matrix[i][j+s-1] == matrix[i+s-1][j] == matrix[i+s-1][j+s-1]:
                return True
    return False

n, m =map(int, input().split())

matrix = [list(map(int, input().strip())) for _ in range(n)]
size = min(n, m)

for i in range(size, 0, -1):
    if find_squre(i):
        print(i**2)
        break


