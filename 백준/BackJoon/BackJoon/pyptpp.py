board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

for sk in skill:
    if sk[0] == 1:
        for i in range(sk[1], sk[3]+1):
            for j in range(sk[2], sk[4]+1):
                board[i][j] -= sk[5]

    else:
        for i in range(sk[1], sk[3]+1):
            for j in range(sk[2], sk[4]+1):
                board[i][j] += sk[5]

answer = 0
for i in board:
    for j in i:
        if j >= 1:
            answer += 1

print(answer)