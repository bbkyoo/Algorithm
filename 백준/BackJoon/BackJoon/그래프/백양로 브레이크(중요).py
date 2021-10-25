# https://steady-coding.tistory.com/103
# 전반적인 로직 
#1. 도로가 양방향이든 일방향이든 u에서 v까지는 무조건 갈 수 있으므로 비용은 0이다.
#(여기서, 비용은 필요한 양방향 도로의 개수로 보면 됩니다.)
#2. 만약, 도로가 일방향일 경우, v에서 u까지 가려면 양방향 도로를 하나 둬야 하므로 비용은 1이다.
#3. 만약, 도로가 양방향일 경우, v에서 u까지 가는 데 비용은 0이다.
#4. 위에서 정의한 배열을 플로이드 와샬 알고리즘을 수행한다. 

import sys

inf = sys.maxsize
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [[inf]*(n) for _ in range(n)] 

# b가 0일 경우 u에서 v로 가는 일방통행 길인 것이고, 
# b가 1일 경우 u와 v를 잇는 양방향 길이다.

for _ in range(m):
    u, v, b = map(int, input().split())
    if b == 0:
        matrix[u-1][v-1] = 0
        matrix[v-1][u-1] = 1
    else:
        matrix[u-1][v-1] = 0
        matrix[v-1][u-1] = 0

for i in range(n):
    matrix[i][i] = 0

K = int(input())

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]
                
for _ in range(K):
    s, e = map(int, input().split())
    print(matrix[s-1][e-1])
