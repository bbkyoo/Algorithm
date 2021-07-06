# 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 3. 화면에 있는 이모티콘 중 하나를 삭제한다.

# visited[화면에 나온 이모티콘 개수][클립보드 이모티콘 개수]

from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    q = deque([])
    q.append([1,0])
    visited[1][0] = 0

    while q:
        x, y = q.popleft()

        if visited[x][x] == -1:     # 1번 연산
            visited[x][x] = visited[x][y] + 1
            q.append([x,x])

        if x+y <= s and visited[x+y][y] == -1: # 2번 연산
            visited[x+y][y] = visited[x][y] + 1
            q.append([x+y,y])

        if x-1 >= 0 and visited[x-1][y] == -1: # 3번 연산
            visited[x-1][y] = visited[x][y] + 1
            q.append([x-1,y])

s = int(input())
visited = [[-1]*(s+1) for _ in range(s+1)]
bfs()

result = visited[s][1]
for i in range(1, s):
    if visited[s][i] != -1:
        result = min(result, visited[s][i])
print(result)





