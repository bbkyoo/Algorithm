import heapq
import sys
inf = sys.maxsize

n, e = map(int, input().split())
s = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    s[a].append([c, b])
    s[b].append([c, a])
    
def dijkstra(start):
    dp = [inf]*(n+1)
    dp[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        w, n = heapq.heappop(heap)

        for wei, n_n in s[n]:
            next_wei = wei + w
            if next_wei < dp[n_n]:
                dp[n_n] = next_wei
                heapq.heappush(heap, [next_wei, n_n])

    return dp

v1, v2 = map(int, input().split())

one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)

cnt = min(one[v1]+v1_[v2]+v2_[n], one[v2]+v2_[v1]+v1_[n])
