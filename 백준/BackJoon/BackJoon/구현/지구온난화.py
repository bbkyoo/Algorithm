dx = [-1,0,1,0]
dy = [0,1,0,-1]

r, c = map(int, input().split())

matrix =[]
visited = [[0]*c for _ in range(r)]

for _ in range(r):
    matrix.append(list(input()))

for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'X':
            cnt = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < r and 0 <= ny < c:
                    if matrix[nx][ny] == '.':
                        cnt += 1
                elif nx < 0 or nx >= r:
                    cnt += 1
                elif ny < 0 or ny >= c:
                    cnt += 1

            if cnt >= 3:
                matrix[i][j] = 'O'

for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'O':
            matrix[i][j] = '.'

while True:
    cnt = 0
    for i in range(r):
        if matrix[i][0] == '.':
            cnt += 1

    if cnt == r:
        for i in range(r):
            matrix[i].pop(0)
    else:
        break

while True:
    cnt = 0
    for i in range(r):
        if matrix[i][-1] == '.':
            cnt += 1

    if cnt == r:
        for i in range(r):
            matrix[i].pop(-1)
    else:
        break

while True:
    cnt = 0
    for i in range(len(matrix[0])):
        if matrix[0][i] == '.':
            cnt += 1

    if cnt == len(matrix[0]):
        matrix.pop(0)
    else:
        break

while True:
    cnt = 0
    for i in range(len(matrix[-1])):
        if matrix[-1][i] == '.':
            cnt += 1

    if cnt == len(matrix[-1]):
        matrix.pop(-1)
    else:
        break

for i in matrix:
    for j in i:
        print(j, end='')
    print()




























