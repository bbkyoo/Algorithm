# S는 양 W는 늑대 D는 울타리 울타리를 쳐서 못가게 하기

r, c = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

flag = False
matrix = []
for _ in range(r):
    matrix.append(list(input()))

for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'W':
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]

                if 0 <= nx < r and 0 <= ny < c:
                    if matrix[nx][ny] == 'S':
                        flag = True
                        break
        elif matrix[i][j] == 'S':
            continue
        else:
            matrix[i][j] = 'D'

if flag:
    print(0)
else:
    print(1)
    for i in matrix:
        print(''.join(i))