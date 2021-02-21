# 8가지 경우의 수(+1, -1, +a, -a, +b, -b, *a, *b)로 bfs를 수행해준다.

from collections import deque
import sys

input = sys.stdin.readline

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1

    while q:
        x = q.popleft()

        for i in range(8):
            if i < 6:
                nx = x + d[i]
                if 0 <= nx <= 100000 and visited[nx] == 0:
                    q.append(nx)
                    visited[nx] = 1
                    s[nx] = s[x] + 1
            else:
                nx = x * d[i]
                if 0 <= nx <= 100000 and visited[nx] == 0:
                    q.append(nx)
                    visited[nx] = 1
                    s[nx] = s[x] + 1

a, b, n, m = map(int, input().split())
d = [1, -1, a, -a, b, -b, a, b]
visited = [0] * 100001
s = [0] * 100001
bfs(n)
print(s[m])
