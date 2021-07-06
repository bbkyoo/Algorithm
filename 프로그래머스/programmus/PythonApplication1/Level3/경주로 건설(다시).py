from collections import deque

def solution(board):
    answer = 999999
    q = deque()
    q.append((0,0,4,0))
    
    visited = {
        (0,0,1):0, # (x, y, 현재위치(x, y)에서 바라보고 있는 방향): 현재위치까지 오는데 드는 비용 
        (0,0,3):0  # 0, 1, 2, 3 | 상 하 좌 우
    }
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x,y,d,c = q.popleft()

        if x == len(board) - 1 and y == len(board) - 1:
            answer = min(answer, c)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board):
                if board[nx][ny] == 0:
                    nc = c
                    if d == 4: # 맨 처음엔 어느 방향으로나 올 수 있으므로 직선도로
                        nc += 100
                    elif d <= 1 and i <= 1: # 바라보는 방향과 진행방향이 세로일 때
                        nc += 100
                    elif d >= 2 and i >= 2: # 바라보는 방향과 진행방향이 가로일 때
                        nc += 100
                    else: # 바라보는 방향과 진행방향이 서로 다를 때
                        nc += 500 + 100

                    if not visited.get((nx, ny, i)) or visited[(nx, ny, i)] > nc:
                        visited[(nx, ny, i)] = nc
                        q.append((nx, ny, i, nc))

    return answer

















