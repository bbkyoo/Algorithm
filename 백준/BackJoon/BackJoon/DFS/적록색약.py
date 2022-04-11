import sys
import copy

input = sys.stdin.readline

def dfs(type, pos, board, visited):
   
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]

    position_list = []
    position_list.append(pos)
    visited[pos[0]][pos[1]] = 1

    while position_list:
        r, c = position_list.pop()
        current_color = board[r][c]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                next_color = board[nr][nc]
                if current_color == next_color:
                    visited[nr][nc] = 1
                    position_list.append((nr, nc))
                    continue

                # 적녹 색약인 경우
                if type == 1 and (current_color == "R" or current_color == "G") and (next_color == "R" or next_color == "G"):
                    visited[nr][nc] = 1
                    position_list.append((nr, nc))

def solve(N, board):
    visited_0 = [[0]*N for i in range(N)]
    visited_1 = [[0]*N for i in range(N)]
    count_0 = 0
    count_1 = 0

    for r in range(N):
        for c in range(N):
            if not visited_1[r][c]:
                dfs(1, (r,c), board, visited_1)
                count_1 += 1
            if not visited_0[r][c]:
                dfs(0, (r,c), board, visited_0)
                count_0 += 1
    
    print(count_0, count_1)


if __name__=="__main__":
    N = int(input())

    board = [list(map(str, input())) for i in range(N)]
    
    solve(N, board)



import copy
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y, matrix, visited):
    q = deque([])
    q.append([x, y])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and matrix[nx][ny] == matrix[x][y]:
                    q.append([nx, ny])
                    visited[nx][ny] = 1

# 최근 풀었던 방법
# n = int(input())
# matrix1 = []
# matrix2 = []
# visited1 = [[0]*n for _ in range(n)]
# visited2 = [[0]*n for _ in range(n)]
# for _ in range(n):
#     matrix1.append(list(input()))
#
# matrix2 = copy.deepcopy(matrix1)
# for i in range(len(matrix2)):
#     for j in range(len(matrix2[i])):
#         if matrix2[i][j] == 'R' or matrix2[i][j] == 'G':
#             matrix2[i][j] = 'R'
#
# num1 = 0
# num2 = 0
# for i in range(n):
#     for j in range(n):
#         if visited1[i][j] == 0:
#             bfs(i, j, matrix1, visited1)
#             num1 += 1
#         if visited2[i][j] == 0:
#             bfs(i, j, matrix2, visited2)
#             num2 += 1
#
# print(num1, num2)