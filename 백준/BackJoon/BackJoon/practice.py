from collections import deque

n = int(input())
m = int(input())

matrix = [[] for _ in range(n+1)]
visited = [0]*(n+1)
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

def bfs(v):
    global result

    q = deque([v])
    visited[v] = 1

    while q:
       v = q.popleft()

       for i in matrix[v]:
           if visited[i] == 0:
               visited[i] = 1
               q.append(i)
               result += 1
bfs(1)
print(result)



