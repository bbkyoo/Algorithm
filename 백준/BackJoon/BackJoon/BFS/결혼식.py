from collections import deque

def bfs(v):
    global count
    
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        
        for i in friend[v]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                visited[i] = visited[v] + 1

n = int(input())
m = int(input())

friend = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

count = 0
bfs(1)

# 1: 본인, 2: 친구, 3: 친구의 친구
for i in range(2, n+1):
    if visited[i] < 4 and visited[i] != 0:
        count += 1

print(count)