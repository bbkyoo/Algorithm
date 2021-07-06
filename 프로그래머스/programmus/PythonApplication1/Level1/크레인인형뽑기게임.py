def solution(board, moves):
    box = []
    count = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if len(box) == 0:
                    box.append(board[j][i-1])
                else:
                    if box[-1] == board[j][i-1]:
                        count += 2
                        box.pop()
                    else:
                        box.append(board[j][i-1])
                board[j][i-1] = 0
                break       

    return count