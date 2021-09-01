import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if matrix[i][j] == 1 or (matrix[i][k] == 1 and matrix[k][j] == 1):
                matrix[i][j] = 1

answer = 0
for i in range(1, n+1):
    known_height = 0
    for j in range(1, n+1):
        known_height += matrix[i][j] + matrix[j][i] # 자신이 가는 경로(자기보다 작은 사람) + 자신에게 오는 경로(자기보다 큰 사람)
    if known_height == n-1:
        answer += 1

print(answer)
