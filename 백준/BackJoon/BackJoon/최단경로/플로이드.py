# https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

import sys

input = sys.stdin.readline
inf = 100000000

n = int(input())
m = int(input())
dp = [[inf]*n for i in range(n)]

for i in range(m):
    a,b,c = map(int, input().split()) # a는 시작, b는 도착, c는 필요한 비용
    if dp[a-1][b-1] > c:
        dp[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and dp[i][j] > dp[i][k] + dp[k][j]: # 플로이드 와샬 알고리즘이다
                dp[i][j] = dp[i][k] + dp[k][j] # k는 거쳐가는 정점이고 i와 j는 시작, 도착 정점이다.
                                               # i에서 j로 가는 최단 경로를 구해주고
                                               # 출력해준다.

for i in dp:
    for j in i:
        if j == inf:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()