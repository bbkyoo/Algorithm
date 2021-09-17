from heapq import heappush, heappop
import sys

input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(start, end):
    heap = []
    heappush(heap, (0, start))
    dp[start] = 0

    while heap:
        w, n = heappop(heap)

        if dp[n] < w:
            continue

        for n_n, wei in graph[n]:
            n_w = w + wei
            if dp[n_n] > n_w:
                dp[n_n] = n_w
                heappush(heap, (n_w, n_n))
                path[n_n] = []
                for p in path[n]:
                    path[n_n].append(p)
                    
                path[n_n].append(n_n)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

dp = [inf]*(n+1)
path = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e,t))

t_s, t_e = map(int, input().split())
path[t_s].append(t_s)

dijkstra(t_s, t_e)

print(dp[t_e])
print(len(path[t_e]))
print(*path[t_e])

