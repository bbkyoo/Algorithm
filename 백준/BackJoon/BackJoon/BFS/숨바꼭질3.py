from collections import deque
import sys

def bfs(n, k):
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            return visited[x]

        for i in (x-1, x+1, x*2):
            if 0 <= i < 100001 and visited[i] == 0:
                if i == 2*x and x != 0:
                    visited[i] = visited[x]
                    q.appendleft(i) # 더 높은 우선순위
                else:
                    visited[i] = visited[x] + 1
                    q.append(i)

n, k = map(int, input().split())

visited = [0] * 100001

print(bfs(n, k))