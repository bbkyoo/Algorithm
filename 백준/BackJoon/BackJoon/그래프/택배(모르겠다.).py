import sys

inf = sys.maxsize

n, m = map(int, input().split())
# 최단 경로를 체크한 리스트 생성
board = [[inf]*n for _ in range(n)]
# 경유지를 체크할 리스트 생성
s = [[0]*n for _ in range(n)]

# 기본 입력 사항 체크
for _ in range(m):
    a, b, t = map(int, input().split())
    board[a-1][b-1] = t
    board[b-1][a-1] = t
    s[a-1][b-1] = b
    s[b-1][a-1] = a


for i in range(n):
    board[i][i] = 0
    s[i][i] = 1

# 모든 경우의 수 체크
for k in range(n):
    for i in range(n):
        for j in range(n):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = min(board[i][j], board[i][k] + board[k][j])
                s[i][j] = s[i][k] # 길이가 갱신될때 맨 처음 s[i][k]를 이어간다.

for i in range(n):
    for j in range(n):
        if i == j:
            print("-", end=' ')
        else:
            print(s[i][j], end=' ')
    print()

