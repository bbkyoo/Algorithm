# 플로이드 와샬 알고리즘(각 위치에서 파티 장소로 가는 최솟값)
# 다익스트라 알고리즘(파티 장소에서 각 위치로 돌아가는 최소 값)
# https://kangmin1012.tistory.com/8

import heapq
import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())
inf = 100000000
s = [[] for _ in range(n+1)]
s_r = [[] for _ in range(n+1)]
dp = [inf]*(n+1)
dp_r = [inf]*(n+1)

def dijkstra(start, dp, s):
    dp[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        w, n = heapq.heappop(heap)
        
        if dp[n] < w:
            continue
        for n_n, wei in s[n]:
            n_w = w + wei
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heapq.heappush(heap, [n_w, n_n])

for _ in range(m):
    a, b, t = map(int, input().split())
    s[a].append([b, t])
    s_r[b].append([a, t])

dijkstra(x, dp, s)
dijkstra(x, dp_r, s_r)
result = 0

for i in range(1, n+1):
    result = max(result, dp[i] + dp_r[i])

print(result)









