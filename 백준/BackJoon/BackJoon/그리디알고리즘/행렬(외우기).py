# https://m.blog.naver.com/PostView.nhn?blogId=pjok1122&logNo=221652193756&proxyReferer=https:%2F%2Fwww.google.com%2F

N, M = map(int, input().split())

A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

def flip(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]


def checkEquality():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False
    return True

count = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            flip(i, j)
            count += 1

if checkEquality():
    print(count)
else:
    print(-1)
   