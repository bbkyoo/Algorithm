from collections import deque

def heavy_bfs(v):
    global total_cnt
    q = deque()
    q.append(v)
    visited = [0]*(n+1)
    visited[v] = 1
    cnt = 0

    while q:
        v = q.popleft()
        for i in heavy_info[v]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                if cnt > standard:
                    total_cnt += 1
                    return
                q.append(i)

def light_bfs(v):
    global total_cnt
    q = deque()
    q.append(v)
    visited = [0]*(n+1)
    visited[v] = 1
    cnt = 0

    while q:
        v = q.popleft()
        for i in light_info[v]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                if cnt > standard:
                    total_cnt += 1
                    return
                q.append(i)

n, m = map(int, input().split())

heavy_info = [[] for _ in range(n+1)]
light_info = [[] for _ in range(n+1)]
standard = n//2
total_cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    heavy_info[b].append(a)
    light_info[a].append(b)

for i in range(1, n+1):
    heavy_bfs(i)
    light_bfs(i)

print(total_cnt)
