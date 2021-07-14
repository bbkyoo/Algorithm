from collections import deque

def solution(n, results):
    def bfs(v, matrix):
        q = deque()
        q.append(v)
        visited = [0]*(n+1)
        visited[v] = 1
        temp = [v]

        while q:
            v = q.popleft()

            for i in matrix[v]:
                if visited[i] == 0:
                    q.append(i)
                    temp.append(i)
                    visited[i] = 1

        return temp

    matrix1 = [[] for _ in range(n+1)]
    matrix2 = [[] for _ in range(n+1)]

    for i in results:
        matrix1[i[1]].append(i[0])
        matrix2[i[0]].append(i[1])
    
    answer = 0
    for i in range(1, n+1):
        if len(set(bfs(i, matrix1) + bfs(i, matrix2))) == n:
            answer += 1

    return answer
   