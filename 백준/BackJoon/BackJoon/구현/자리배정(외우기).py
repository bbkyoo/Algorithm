import sys

input = sys.stdin.readline

#m, n = map(int, input().split())
#k = int(input())

#matrix = [[0]*m for _ in range(n)]

#a = n
#b = m
#x = n 
#y = 0
#num = 0

#i = 0

#while True:
#    isTrue = True
#    for q in matrix:
#        for w in q:
#            if w == 0:
#                isTrue = False

#    if isTrue:
#        break

#    x -= 1
#    for i in range(a):
#        num += 1
#        matrix[x-i][y] = num
#    x -= i        
    
#    for i in range(1, b):
#        num += 1
#        matrix[x][y+i] = num
#    y += i

#    for i in range(1, a):
#        num += 1
#        matrix[x+i][y] = num
#    x += i    

#    for i in range(1, b-1):
#        num += 1
#        matrix[x][y-i] = num
#    y -= i

#    a -= 2
#    b -= 2

#tr = False
#for i in range(len(matrix)):
#    for j in range(len(matrix[i])):
#        if matrix[i][j] == k:
#            print(n-i, j+1)
#            tr = True
#            break

#    if tr:
#        break

#if tr == False:
#    print(0)

def is_wall(i, j):
    global l_wall, r_wall, u_wall, d_wall
    
    if i == u_wall:
        l_wall += 1
        return True

    if i == d_wall:
        r_wall -= 1
        return True

    if j == l_wall:
        d_wall -= 1
        return True

    if j == r_wall:
        u_wall += 1
        return True

    return False

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

c, r = map(int, input().split())
k = int(input())

maps =[[0]*c for _ in range(r)]
cnt = 1

l_wall = 0
r_wall = r+1
u_wall = 0
d_wall = c+1
d = 0
i = 1
j = 1

if k > r*c:
    print(0)
else:
    while True:
        if cnt == k:
            print(i, j)
            break

        if is_wall(i+dx[d], j+dy[d]):
            d += 1
            d %= 4
        i += dx[d]
        j += dy[d]
        cnt += 1























