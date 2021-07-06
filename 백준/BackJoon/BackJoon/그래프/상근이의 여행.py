from collections import deque

t = int(input())

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    count = 0

    while q:
        v = q.popleft()
        for i in matrix[v]:
            if visited[i] == 0:
                visited[i] = 1
                count += 1
                q.append(i)
            
    return count

for _ in range(t):
    n, m = map(int, input().split())
    matrix = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for _ in range(m):
        a, b = map(int, input().split())
        matrix[a].append(b)
        matrix[b].append(a)

    result = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            result += bfs(i)

    print(result)
    













