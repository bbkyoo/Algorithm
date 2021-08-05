import heapq

def dijkstra(start,dp,graph):
    dp[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        wei, now = heapq.heappop(heap)
        for w, next_node in graph[now]:
            next_wei = w + wei
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))

def solution(N, road, K):
    inf = 100000000

    dp = [inf] * (N+1)
    graph = [[] for _ in range(N+1)]

    for i in range(len(road)):
        graph[road[i][0]].append((road[i][2],road[i][1]))
        graph[road[i][1]].append((road[i][2],road[i][0]))

    dijkstra(1,dp,graph)
    count = 0
    for i in range(1, N+1):
        if dp[i] <= K:
            count += 1

    return count


