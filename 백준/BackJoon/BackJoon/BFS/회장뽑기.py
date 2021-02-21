# 어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다. 어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나 친구의 친구임을 말한다. 
# 또한 어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친구의 친구의 친구임을 말한다.
# 회장은 회원들 중에서 점수가 가장 작은 사람이 된다. 회장의 점수와 회장이 될 수 있는 모든 사람을 찾는 프로그램을 작성하시오
# 플로이드 와샬
from collections import deque
import sys

inf = sys.maxsize
input = sys.stdin.readline

n = int(input())
matrix = [[inf]*(n+1) for _ in range(n+1)]

while True:
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        break
    matrix[x][y] = 1
    matrix[y][x] = 1

for i in range(1, n+1):
    matrix[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if matrix[i][j] == 1 or matrix[i][j] == 0:
                continue
            elif matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

answer = []
for i in range(1, n+1):
    answer.append(max(matrix[i][1:]))

result = min(answer)
print(result, answer.count(result))

for i, v in enumerate(answer):
    if v == result:
        print(i+1, end=" ")










