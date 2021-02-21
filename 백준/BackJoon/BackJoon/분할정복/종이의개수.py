n = int(input())

paper = []

for i in range(n):
    paper.append(list(map(int, input().split())))

minus = 0
zero = 0
one = 0

def divide(x,y,n):
    global minus, zero, one
    check = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != paper[i][j]:
                divide(x,y, n//3)
                divide(x + n//3,y, n//3)
                divide(x + 2*(n//3),y, n//3)
                divide(x,y + n//3, n//3)
                divide(x,y + 2*(n//3), n//3)
                divide(x + n//3,y + n//3, n//3)
                divide(x + 2*(n//3),y + n//3, n//3)
                divide(x + (n//3),y + 2*(n//3), n//3)
                divide(x + 2*(n//3),y + 2*(n//3), n//3)
                return

    if check == -1:
        minus += 1
        return
    elif check == 0:
        zero += 1
        return
    else:
        one += 1
        return

divide(0,0,n)
print(minus)
print(zero)
print(one)

