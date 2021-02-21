def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], min(board[i-1][j], board[i][j-1])) + 1

    return max(num for row in board for num in row)**2



