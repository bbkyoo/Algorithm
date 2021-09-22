import heapq
import sys

input = sys.stdin.readline
inf = sys.maxsize

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

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    dp = [inf]*(n+1)
    heap = []
    graph = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, input().split()) # 어떤 컴퓨터 a가 다른 컴퓨터 b에 의존한다면, b가 감염되면 그로부터 일정 시간 뒤 a도 감염되고 만다.
        graph[b].append((s, a))

    dijkstra(c)

    max_value = 0
    cnt = 0
    for i in dp:
        if i != inf:
            cnt += 1
            max_value = max(max_value, i)

    print(cnt, max_value)









