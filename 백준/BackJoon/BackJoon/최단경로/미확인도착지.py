# g와 h를 무조건 지나야 한다면 두가지 방법이 있다.
# 출발지점 -> g -> h -> 도착지점 혹은
# 출발지점 -> h -> g -> 도착지점 이 될 수 있다.
# 이 두가지의 최단 거리를 구해주고 그 최단거리중 하나가
# 출발지점 -> 도착지점의 최단거리와 같다면 도착지점을 저장해준다.

import heapq
import sys

input = sys.stdin.readline
inf = 100000000

T = int(input())

def dijkstra(start):
    dp = [inf]*(n+1)
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

for _ in range(T):
    n, m, t = map(int, input().split()) # 교차로, 도로, 목적지
    s, g, h = map(int, input().split()) # 출발지, g, h, 교차로
    matrix = [[] for i in range(n+1)]
    
    x_list = []
    for _ in range(m):
        a, b, d = map(int, input().split()) # a와 b 사이의 d의 양방향 도로가 있다.
        matrix[a].append((b,d))
        matrix[b].append((a,d))
    for _ in range(t):
        x = int(input())
        x_list.append(x)
    st = dijkstra(s)
    g_ = dijkstra(g)
    h_ = dijkstra(h)
    cnt = [] 
    for i in x_list:
        if st[g] + g_[h] + h_[i] == st[i] or st[h] + h_[g] + g_[i] == st[i]:
            cnt.append(i)
        
    cnt.sort()
   
    for i in cnt:
        print(i, end=' ')
    print()


