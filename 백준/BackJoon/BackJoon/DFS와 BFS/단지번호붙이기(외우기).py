#home = []
#for i in range(N):
#    home.append(list(input())) # 이렇게 해야 2중 리스트 안의 모든 원소들이 다 나누어서 출력가능해진다.

import sys

N = int(input())
# 데이터 저장용 공간 matrix
matrix = [[0]*N for _ in range(N)]
# 방문내역 저장용 visited
visited = [[0]*N for _ in range(N)]

# matrix에 아파트 유무 0과 1저장
for i in range(N):
    line = input().strip()
    for j, b in enumerate(line):
        matrix[i][j] = int(b)

# 방향 확인용 좌표 dx와 dy
# 중앙을 기준으로 좌/우/위/아래
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# DFS 함수 정의
def dfs(x, y, c):
    visited[x][y] = 1 # 방문 여부 표시
    global nums         # 아파트 단지 수를 세기위한 변수

    # 아파트가 있으면 숫자를 세어줍니다
    if matrix[x][y] == 1:
        nums += 1

    # 해당 위치에서 좌/우/위/아래 방향의 좌표를 확인해서 dfs 적용
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i] 
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                dfs(nx, ny, c)

count = 1 # 아파트 단지를 세기 위한
numlist = [] # 아파트 단지별 숫자
nums = 0 # 아파트 수
for a in range(N):
    for b in range(N):
        if matrix[a][b] == 1 and visited[a][b] == 0:
            dfs(a,b,count)
            numlist.append(nums)
            nums = 0
            count += 1

print(len(numlist))
for n in sorted(numlist):
    print(n)




































