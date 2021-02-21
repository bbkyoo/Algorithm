# 왜 런타임 에러가 날까.................................

king, rock, n = map(str,input().split())

matrix = [['A'+str(i) ,'B'+str(i),'C'+str(i),'D'+str(i),'E'+str(i),'F'+str(i),'G'+str(i),'H'+str(i)] for i in range(8,0,-1)]

king_x = 0
king_y = 0
rock_x = 0
rock_y = 0
for i in range(8):
    for j in range(8):
        if matrix[i][j] == king:
            king_x = i
            king_y = j
        elif matrix[i][j] == rock:
            rock_x = i
            rock_y = j

for _ in range(int(n)):
    move = input()
    if move == 'R':
        if king_y != 7 and rock_y != 7:
            king_y += 1
            rock_y += 1
        else:
            continue
    elif move == 'RT':
        if king_y != 7 and king_x != 0 and rock_y != 7 and rock_x != 0:
            king_y += 1
            rock_y += 1
            king_x -= 1
            rock_x -= 1
        else:
            continue
    elif move == 'RB':
        if king_y != 7 and king_x != 0 and rock_y != 7 and rock_x != 0:
            king_y += 1
            rock_y += 1
            king_x += 1
            rock_x += 1
        else:
            continue
    elif move == 'L':
        if king_y != 0 and rock_y != 0:
            king_y -= 1
            rock_y -= 1
        else:
            continue

    elif move == 'LT':
        if king_y != 0 and king_x != 0 and rock_y != 0 and rock_x != 0:
            king_y -= 1
            rock_y -= 1
            king_x -= 1
            rock_x -= 1
        else:
            continue
    elif move == 'LB':
        if king_y != 0 and king_x != 7 and rock_y != 0 and rock_x != 7:
            king_y -= 1
            rock_y -= 1
            king_x += 1
            rock_x += 1
        else:
            continue
    elif move == 'B':
        if king_x != 7 and rock_x != 7:
            king_x += 1
            rock_x += 1
        else:
            continue
    elif move == 'T':
        if king_x != 0 and rock_x != 0:
            king_x -= 1
            rock_x -= 1
        else:
            continue

print(matrix[king_x][king_y])
print(matrix[rock_x][rock_y])
