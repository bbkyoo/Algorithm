from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        v = q.popleft()

        for i in matrix[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                dist[i] = dist[v] + 1

n, m, k, x = map(int, input().split())

matrix = [[] for _ in range(n+1)]
visited = [0]*(n+1)
dist = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
bfs(x)
result = []
for i in range(1, len(dist)):
    if dist[i] == k:
        result.append(i)
result.sort()

if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)