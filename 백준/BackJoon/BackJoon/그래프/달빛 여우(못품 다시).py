import sys
import heapq
inf = sys.maxsize
input = sys.stdin.readline

def dijkstra_fox():
    dist = [inf]*(n+1) 
    dist[1] = 0
    q = []
    heapq.heappush(q, (dist[1], 1))

    while q:
        wei, now = heapq.heappop(q)
        if dist[now] < wei:
            continue

        for w, next_node in matrix[now]:
            next_wei = w + wei
            if dist[next_node] > next_wei:
                dist[next_node] = next_wei
                heapq.heappush(q, (dist[next_node], next_node))

    return dist

def dijkstra_wolf():
    # dist[0] 빠르게 도착 / dist[1] 느리게 도착
    dist = [[inf]*(n+1) for _ in range(2)] 
    dist[1][1] = 0
    q = []
    heapq.heappush(q, (dist[1][1], 1, False))

    while q:
        wei, now, bl = heapq.heappop(q)
        if bl and dist[0][now] < wei:
            continue

        elif not bl and dist[1][now] < wei:
            continue

        for w, next_node in matrix[now]:
            if bl: # 빠르게 도착했다면, 느리게 출발
                next_wei = wei + (w*2)
                if next_wei < dist[1][next_node]:
                    dist[1][next_node] = next_wei
                    heapq.heappush(q, (dist[1][next_node], next_node, False))
            else: # 느리게 도착했다면, 빠르게 출발
                next_wei = wei + (w//2)
                if next_wei < dist[0][next_node]:
                    dist[0][next_node] = next_wei
                    heapq.heappush(q, (dist[0][next_node], next_node, True))

    return dist


n, m = map(int, input().split())
matrix = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    matrix[a].append((d*2, b))
    matrix[b].append((d*2, a))

fox = dijkstra_fox()
wolf = dijkstra_wolf()

answer = 0

for i in range(1, n+1):
    if fox[i] < min(wolf[0][i], wolf[1][i]):
        answer += 1

print(answer)