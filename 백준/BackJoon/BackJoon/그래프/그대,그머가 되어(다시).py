from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 0

    while q:
        v = q.popleft()

        if v == b:
            return visited[v]

        for i in matrix[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                q.append(i)

    return -1

a, b = map(int, input().split())
n, m = map(int, input().split())

matrix = [[] for _ in range(n+1)]
visited = [-1]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)

print(bfs(a))




