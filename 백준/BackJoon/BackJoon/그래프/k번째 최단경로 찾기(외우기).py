import sys
import heapq
inf = sys.maxsize

input = sys.stdin.readline

def dijkstra(start):
    heapq.heappush(heap, (0, start))
    dp[start][0] = 0     

    while heap:
        w, n = heapq.heappop(heap)
        for n_n, wei in matrix[n]:
            n_w = wei + w
            if n_w < dp[n_n][k-1]:
                dp[n_n][k-1] = n_w
                dp[n_n].sort()                
                heapq.heappush(heap, (n_w, n_n))

n, m, k = map(int, input().split())

dp = [[inf]*k for _ in range(n+1)]
heap = []
matrix = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split()) 
    matrix[a].append((b, c))

dijkstra(1)
for i in range(1, n+1):
    if dp[i][k-1] == inf:
        print(-1)
    else:
        print(dp[i][k-1])