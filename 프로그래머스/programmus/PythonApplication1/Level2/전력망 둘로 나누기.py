from collections import deque

def solution(n, wires):
    def bfs(v):
        cnt = 0
        q = deque([])
        q.append(v)
        visited = [0] * (n + 1)
        visited[v] = 1
        while q:
            v = q.popleft()
            for i in matrix[v]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
                    cnt += 1
        return cnt

    result = 1e9
    for i in range(len(wires)):
        matrix = [[] for _ in range(n + 1)]

        for j in range(len(wires)):
            if i == j:
                continue
            else:
                matrix[wires[j][0]].append(wires[j][1])
                matrix[wires[j][1]].append(wires[j][0])

        mx = 0
        mn = 1e9
        for i in range(1, n+1):
            if mx < bfs(i):
                mx = bfs(i)
            if mn > bfs(i):
                mn = bfs(i)

        result = min(result, abs(mx - mn))

    return result