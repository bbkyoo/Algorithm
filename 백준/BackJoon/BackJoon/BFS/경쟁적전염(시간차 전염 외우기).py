# S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램
# 다 같이 처음부터 q에 넣어주면 시간차로 순서대로 bfs가 적용이 되는 개념을 이용한 것

from collections import deque
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(data):
    data.sort()
    q = deque(data)

    while q:
        virus, s, x, y = q.popleft()

        if s == target_s:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = virus 
                    q.append([virus, s+1, nx, ny])

n, k = map(int, input().split())

matrix = []
data = []

for i in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

    for j in range(n):
        if line[j] != 0:
            # 바이러스 종류, 시간, 위치 삽입
            data.append([line[j], 0, i, j])

target_s, target_x, target_y = map(int, input().split())

bfs(data)

print(matrix[target_x-1][target_y-1])
