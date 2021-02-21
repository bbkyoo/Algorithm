import sys

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