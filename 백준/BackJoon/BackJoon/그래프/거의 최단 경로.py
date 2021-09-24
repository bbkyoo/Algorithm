# https://jjangsungwon.tistory.com/98

import sys
import heapq
from collections import deque
inf = sys.maxsize

def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        wei, now = heapq.heappop(heap)

        if dp[now] < wei:
            continue

        for w, next_node in graph[now]:
            next_wei = wei + w
            if dp[next_node] > next_wei:
                dp[next_node] = next_wei 
                heapq.heappush(heap, (next_wei ,next_node))

def bfs():
    q = deque()
    q.append(d)
    while q:
        v = q.popleft()
        if v == s:
            continue
        for pre_v, pre_c in r_graph[v]:
            if dp[pre_v] + graph[pre_v][v] == dp[v]:
                if (pre_v, v) not in remove_list:
                    remove_list.append((pre_v, v))
                    q.append(pre_v)

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    s, d = map(int, input().split())

    heap = []
    graph = [dict() for _ in range(n+1)]
    r_graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u][v] = p
        r_graph[u].append((v, p))

    dp = [inf]*(n+1)
    dijkstra(s)
    
    remove_list = list()
    bfs()

    for u, v in remove_list:
        del graph[u][v]

    dp = [inf]*(n+1)
    dijkstra(s)

    if dp[d] == inf:
        print(-1)
    else:
        print(dp[d])