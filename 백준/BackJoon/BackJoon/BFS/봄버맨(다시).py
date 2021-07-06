dx = [0,1,0,-1]
dy = [1,0,-1,0]

r, c, n = map(int, input().split())
A = [list(input()) for _ in range(r)]
old = []

def full():
    return [['O' for _ in range(c)] for _ in range(r)]

def bomb(A, old):
    for i in range(r):
        for j in range(c):
            if old[i][j] == '.':
                continue
            A[i][j] = '.'
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if not (0 <= nx < r and 0 <= ny < c):
                    continue
                A[nx][ny] = '.'

    return A

def tictoc(t):
    global A, old
    if t % 2:
        A, old = bomb(A, old), A[:]
    else:
        A, old = full(), A[:]

for i in range(n-1):
    tictoc(i)

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end="")
    print()