from collections import deque

def solution(n, vertex):
    def bfs(v):
        q = deque()
        q.append(v)
        visited[v] = 1
    
        while q:
            v = q.popleft()

            for i in matrix[v]:
                if visited[i] == 0:
                    dist[i] = dist[v] + 1
                    q.append(i)
                    visited[i] = 1

    matrix = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    dist = [0] * (n+1)

    for i in vertex:
        matrix[i[0]].append(i[1])
        matrix[i[1]].append(i[0])

    bfs(1)
    result = 0
    mx = max(dist)
    for i in dist:
        if i == mx:
            result += 1

    return result


