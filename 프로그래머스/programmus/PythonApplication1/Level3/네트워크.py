from collections import deque

def solution(n, computers):
    def bfs(v):
        q = deque()
        q.append(v)
        visited[v] = 1
        answer = [v]

        while q:
            v = q.popleft()

            for i in range(n):
                if computers[v][i] == 1 and visited[i] == 0:
                    answer.append(i)
                    q.append(i)
                    visited[i] = 1

        return answer
    visited = [0]*(n)
    result = []
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if (computers[i][j] == 1) and (visited[i] == 0):
                result.append(bfs(i))
    
    return len(result)

