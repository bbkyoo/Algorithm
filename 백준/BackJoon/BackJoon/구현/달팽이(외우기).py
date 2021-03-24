n = int(input())
target = int(input())

matrix = [[0]*n for _ in range(n)]
x = n // 2
y = n // 2
check = 2
num = 1

matrix[x][y] = num

i = 0

while matrix[0][0] != n**2:
    x -= 1
    for i in range(check):
        num += 1
        matrix[x][y+i] = num
        if num == target:
            ans = [x+1, y+i+1]
    y += i

    for i in range(1, check+1):
        num += 1
        matrix[x+i][y] = num
        if num == target:
            ans = [x+i+1, y+1]
    x += i

    for i in range(1, check+1):
        num += 1
        matrix[x][y-i] = num
        if num == target:
            ans = [x+1, y-i+1]
    y -= i

    for i in range(1, check+1):
        num += 1
        matrix[x-i][y] = num
        if num == target:
            ans = [x-i+1, y+1]
    x -= i
    check += 2

for i in matrix:
    for j in i:
        print(j, end=" ")
    print()

print(*ans)
















