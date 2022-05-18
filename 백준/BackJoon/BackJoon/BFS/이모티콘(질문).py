# https://it-garden.tistory.com/324
# 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 화면에 있는 이모티콘 중 하나를 삭제한다.

from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([1, 0])
    ch[1][0] = 0    

    while q:
        x, y = q.popleft()

        if ch[x][x] == -1:  #1번 연산
            ch[x][x] = ch[x][y] + 1
            q.append([x, x])
        if x + y <= s and ch[x+y][y] == -1: # 2번 연산
            ch[x+y][y] = ch[x][y] + 1
            q.append([x+y, y])
        if x-1 >= 0 and ch[x-1][y] == -1: # 3번 연산
            ch[x-1][y] = ch[x][y] + 1
            q.append([x-1, y])

s = int(input())

ch = [[-1]*(s+1) for i in range(s+1)] 

bfs()

r = ch[s][1]
for i in range(1,s):
    if ch[s][i] != -1:
        r = min(r, ch[s][i])

print(r)


