import sys
from collections import deque

input = sys.stdin.readline

def bfs(M, N, box):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    days = -1

    while ripe:
        days += 1
        for _ in range(len(ripe)):
            x,y = ripe.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                    box[nx][ny] = box[x][y] + 1
                    ripe.append([nx, ny])
                    
    for b in box:
        if 0 in b:
            return -1
    return days

m, n = map(int, input().split())

box = []
ripe = deque()

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            ripe.append([i,j])  #이 알고리즘으로 인덱스 i와 j를 찾는다
    box.append(row) # 그리고 box에 row를 넣는다.

print(bfs(m,n,box))