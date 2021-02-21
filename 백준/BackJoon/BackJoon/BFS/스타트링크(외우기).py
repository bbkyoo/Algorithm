# 스타트링크는 총 F층으로 이루어진 고층 건물에 사무실
# 강호가 지금 있는 곳은 S층
# 스타트링크가 있는 곳의 위치는 G층
# U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼
# 강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지, G층에 갈 수 없다면, "use the stairs
from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1
    while q:
        x = q.popleft()
        for i in range(2):
            nx = x + dire[i]
            if 0 <= nx < F and visited[nx] == 0:
                q.append(nx)
                visited[nx] = 1
                matrix[nx] = matrix[x] + 1

F, S, G, U, D = map(int, input().split())
matrix = [-1 for i in range(F)]
visited = [0 for i in range(F)]
dire = [U, -D]
matrix[S-1] = 0
bfs(S-1)

if matrix[G-1] == -1:
    print("use the stairs")
else:
    print(matrix[G-1])

