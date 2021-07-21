import sys
from collections import deque

input = sys.stdin.readline

def bfs(mid):
    visited[start] = 1
    q = deque()
    q.append(start)

    while q:
        v = q.popleft()
        if v == end:
            return True

        for nx, nc in s[v]:
            if visited[nx] == 0 and mid <= nc:
                q.append(nx)
                visited[nx] = 1

    return False

n, m = map(int, input().split())

s = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    s[a].append([b,c])
    s[b].append([a,c])

start, end = map(int, input().split())
low, high = 1, 1000000000
while low <= high:
    visited = [0 for _ in range(n+1)] 
    mid = (low + high)//2
    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1

print(high)