from collections import deque

def bfs(v):
    global ans
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        for i in node[v]:
            if visited[i] == 0:
                ans[i] = v
                visited[i] = 1
                q.append(i)
                
n = int(input())

node = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int ,input().split())
    node[a].append(b)
    node[b].append(a)

ans = [0] * (n+1)
bfs(1)

for i in ans[2:]:
    print(i)
    