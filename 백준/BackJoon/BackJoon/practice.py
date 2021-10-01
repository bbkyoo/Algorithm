from collections import deque

def bfs(v):
    global cnt

    q = deque([])
    q.append(v)
    visited[v] = 1

    while q:
        v = q.popleft()
        cnt += 1

        for i in matrix[v]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)

n = int(input())
m = int(input())
matrix = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

bfs(1)
print(cnt-1)