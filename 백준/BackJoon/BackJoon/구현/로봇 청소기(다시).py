import sys

input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def clean(x, y, d):
    global ans

    if matrix[x][y] == 0:
        matrix[x][y] = 2
        ans += 1

    for _ in range(4):
        nd = (d+3) % 4 #이동 방향을 문제의 조건대로 북동남서 순으로 만들면 현재 방향 + 3을 4로 나눈 나머지가 왼쪽 방향이다
                         # 왼쪽방향이 0이면 clean 함수에 다음 좌표와 방향을 입력한다
        nx = x + dx[nd]
        ny = y + dy[nd]
        if matrix[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd

    nd = (d + 2) % 4 # 4방향 모두 이동할 수 없으면 뒤로 이동할 수 있는지 확인한다
                     # 현재 방향 + 2를 4로 나눈 나머지가 뒤로 이동이다
    nx = x + dx[nd]
    ny = y + dy[nd]

    if matrix[nx][ny] == 1: # 뒤가 벽이면 바로 종료하고 이동할 수 있으면 다음 좌표와 방향을 입력한다               
        return              # 이 때 방향은 유지한 채로 뒤로 이동한 것이기 때문에 nd가 아니라 d를 입력한다
    clean(nx, ny, d)

n, m = map(int, input().split())
x, y, d = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

ans = 0
clean(x, y, d)
print(ans)





