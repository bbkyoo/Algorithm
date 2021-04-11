def pos(y, x):
    global r, c
    return 0 <= y < r and 0 <= x < c 

r, c = map(int, input().split())
k = int(input())

matrix = [[0]*c for _ in range(r)]

for _ in range(k):
    br, bc = map(int, input().split())
    matrix[br][bc] = 1

sr, sc = map(int, input().split())
d = list(map(int, input().split()))

for i in range(4):
    if d[i] == 1:
        d[i] = [-1, 0]
    elif d[i] == 2:
        d[i] = [1, 0]
    elif d[i] == 3:
        d[i] = [0, -1]
    elif d[i] == 4:
        d[i] = [0, 1]

to = 0
moved = True

while moved:
    moved = False

    for i in range(4):
        nr = sr + d[(to + i) % 4][0]
        nc = sc + d[(to + i) % 4][1]
        if pos(nr, nc) and matrix[nr][nc] != 1:
            matrix[sr][sc] = 1
            to = (to + i) % 4
            moved = True
            sr = nr
            sc = nc
            break

print(sr, sc)









