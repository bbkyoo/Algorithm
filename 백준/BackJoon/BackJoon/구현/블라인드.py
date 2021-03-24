m, n = map(int, input().split())

matrix = []
for _ in range(5*m + 1):
    matrix.append(list(input()))

case1 = [['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.']]
case2 = [['*','*','*','*'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.']]
case3 = [['*','*','*','*'],['*','*','*','*'],['.','.','.','.'],['.','.','.','.']]
case4 = [['*','*','*','*'],['*','*','*','*'],['*','*','*','*'],['.','.','.','.']]
case5 = [['*','*','*','*'],['*','*','*','*'],['*','*','*','*'],['*','*','*','*']]

answer = [0,0,0,0,0]

def confirm(i, j):
    temp = []

    for ti in range(i, i+4):
        t = []
        for tj in range(j, j+4):
            t.append(matrix[ti][tj])
        temp.append(t)

    return temp    

for i in range(1, 5*m + 1, 5):
    for j in range(1, 5*n + 1, 5):
        if matrix[i][j] != '#':
            temp = confirm(i, j)
            if temp == case1:
                answer[0] += 1
            elif temp == case2:
                answer[1] += 1
            elif temp == case3:
                answer[2] += 1
            elif temp == case4:
                answer[3] += 1
            else:
                answer[4] += 1

print(*answer)









