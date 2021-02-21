# 힙에 관한 링크
# https://www.daleseo.com/python-heapq/

import heapq
import sys

input = sys.stdin.readline
inf = 100000000

V, E = map(int, input().split()) # V -> 1 ~ V 까지 정점의 개수,  E -> 간선의 개수
k = int(input()) # 시작 정점
dp = [inf]*(V+1)
heap = []
graph = [[] for _  in range(V+1)] 

def dijkstra(start):
    
    dp[start] = 0
    heapq.heappush(heap, (0, start))
    
    while heap:
        wei, now = heapq.heappop(heap)
        for w, next_node in graph[now]:
            next_wei = w + wei
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))

for i in range(E):
    u,v,w = map(int, input().split()) # u -> v로 가중치가 w
    graph[u].append((w,v))

dijkstra(k)

for i in range(1, V+1):
    print("INF" if dp[i] == inf else dp[i])
    

