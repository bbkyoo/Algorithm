from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    global k

    q = deque()
    q.append(v)
    visited[v] = 1
    result = []

    while q:
        v = q.popleft()

        for i in matrix[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                dist[i] += dist[v] + 1

    for i in range(len(dist)):
        if dist[i] == k:
            result.append(i)

    return result                

n, m, k, x = map(int, input().split())
matrix = [[] for _ in range(n+1)]
dist = [0] * (n+1)
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)

result = bfs(x)
result.sort()

if len(result) == 0:
    print(-1)
else:
    for i in range(len(result)):
        print(result[i], end='\n')

