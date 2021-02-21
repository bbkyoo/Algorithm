import heapq
import sys

input = sys.stdin.readline
inf = 100000000

N, E = map(int ,input().split()) # N은 정점의 개수, E은 간선의 개수

matrix = [[] for i in range(N+1)]

def dijkstra(start):
    dp = [inf] * (N+1)
    dp[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        wei, now = heapq.heappop(heap)
        for next_node, w in matrix[now]:
            next_wei = w + wei
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))

    return dp

for i in range(E):
    a, b, c = map(int, input().split())
    matrix[a].append((b,c))
    matrix[b].append((a,c))

v1, v2 = map(int, input().split())

one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)

cnt = min(one[v1] + v1_[v2] + v2_[N], one[v2] + v2_[v1] + v1_[N])

print(cnt if cnt < inf else -1)