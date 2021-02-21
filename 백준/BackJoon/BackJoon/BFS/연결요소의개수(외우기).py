# 1 -> 2 로 간선이 연결되면 대칭하여 똑같이 연결된것을 표현하기 위해 adj[u].append(v), adj[v].append(u) 처럼 했다
import sys
input = sys.stdin.readline

def bfs(v):
    q= [v]
    while q:
        v = q.pop(0)
        for i in matrix[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

def dfs(v):
    visited[v] = 1    
    for i in matrix[v]:
        if not visited[i]:
            dfs(i)


N, M = map(int, input().split())

matrix = [[] for i in range(N+1)]
visited = [0]* (N+1)

for i in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)