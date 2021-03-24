#import sys

#input = sys.stdin.readline

#board =[]

#for _ in range(19):
#    board.append(list(map(int, input().split())))

#answer = 0
#x = 0
#y = 0

#for i in range(19):
#    black = 0
#    white = 0

#    for j in range(19):
#        if board[i][j] == 1:
#            black += 1
#        else:
#            if black == 5:
#                x = i
#                y = j - 5
#                break
#            else:
#                black = 0
        
#        if board[i][j] == 2:
#            white += 1
#        else:
#            if white == 5:
#                x = i
#                y = j - 5
#                break
#            else:
#                white = 0
    
#    if black == 5:
#        answer = 1
#        break

#    elif white == 5:
#        answer = 2
#        break

#for i in range(19):
#    black = 0
#    white = 0

#    for j in range(19):
#        if board[j][i] == 1:
#            black += 1
#        else:
#            if black == 5:
#                x = i - 5
#                y = j 
#                break
#            else:
#                black = 0
        
#        if board[j][i] == 2:
#            white += 1
#        else:
#            if white == 5:
#                x = i - 5 
#                y = j 
#                break
#            else:
#                white = 0
        
#    if black == 5:
#        answer = 1
#        break
#    elif white == 5:
#        answer = 2
#        break

#for i in range():
#    for j in range():

import sys

input = sys.stdin.readline

dx = [0, 1, 1, 1]
dy = [1, 0, -1, 1]

black = []
white = []

for i in range(1, 20):
    board = list(map(int, input().split()))
    for j in range(len(board)):
        if board[j] == 1:
            black.append([i, j+1])
        elif board[j] == 2:
            white.append([i, j+1])

# black부터 찾아보자
for b in black:
    x, y = b
    for i in range(4):
        nx, ny = x, y
        cnt = 1

        while 0 <= nx < 20 and 0 <= ny < 20:
            if [nx+ dx[i], ny+dy[i]] in black:
                cnt += 1
                nx += dx[i]
                ny += dy[i]
            else:
                break

            if cnt >= 5:
                break

        if cnt == 5:
            if [nx + dx[i], ny + dy[i]] not in black:
                if 1 <= x - dx[i] < 20 and 1 <= y - dy[i] < 20:
                    if [x - dx[i], y - dy[i]] not in black:
                        if i != 2:
                            print(1)
                            print(x, y)
                            sys.exit()
                        else:
                            print(1)
                            print(nx, ny)
                            sys.exit()

                else:
                    if i != 2:
                        print(1)
                        print(x,y)
                        sys.exit()
                    else:
                        print(1)
                        print(nx, ny)
                        sys.exit()

for w in white:
    x, y = w
    for i in range(4):
        nx, ny = x, y
        cnt = 1

        while 0 <= nx < 20 and 0 <= ny < 20:
            if [nx+ dx[i], ny+dy[i]] in white:
                cnt += 1
                nx += dx[i]
                ny += dy[i]
            else:
                break

            if cnt >= 5:
                break

        if cnt == 5:
            if [nx + dx[i], ny + dy[i]] not in white:
                if 1 <= x - dx[i] < 20 and 1 <= y - dy[i] < 20:
                    if [x - dx[i], y - dy[i]] not in white:
                        if i != 2:
                            print(2)
                            print(x, y)
                            sys.exit()
                        else:
                            print(2)
                            print(nx, ny)
                            sys.exit()

                else:
                    if i != 2:
                        print(2)
                        print(x,y)
                        sys.exit()
                    else:
                        print(2)
                        print(nx, ny)
                        sys.exit()

print(0)





































