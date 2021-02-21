from collections import deque
import sys

input = sys.stdin.readline

def bfs(s):
    count = 0
    q = deque()
    q.append([s,count])
    
    visited = [0]*300001

    while q:
        v = q.popleft()
        s = v[0]
        count = v[1]

        if not visited[s]:
            visited[s] = 1
            if s == e:
                return count
            count += 1
            if (s + 1) <= 300000:
                q.append([s+1, count])
            if (s - 1) >= 2:
                q.append([s-1, count])
            if matrix[s]:
                if matrix[s][0] <= 300000:
                    q.append([matrix[s][0], count])

    return count
        
n, m = map(int, input().split())
s, e = map(int, input().split())
matrix = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)

print(bfs(s))





