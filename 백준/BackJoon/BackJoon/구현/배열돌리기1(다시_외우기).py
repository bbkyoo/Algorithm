# https://velog.io/@gkscodus11/%EB%B0%B1%EC%A4%80-16926-%EB%B0%B0%EC%97%B4-%EB%8F%8C%EB%A6%AC%EA%B8%B0-1

import sys

input = sys.stdin.readline

def rotate(p, ll, rl, ul, dl):
    x, y = p, p
    d = 0
    while True:
        x, y = x+dx[d], y+dy[d]

        if x == ul or x == dl or y == ll or y == rl:
            x, y = x - dx[d], y - dy[d]
            d += 1
            x, y = x + dx[d], y + dy[d]

        if x == p and y == p:
            return
        
        matrix[p][p], matrix[x][y] = matrix[x][y], matrix[p][p]

n, m, r = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for p in range(min(n,m) // 2):
    for _ in range(r%(2*(n + m - 4*p - 2))):
        rotate(p, p-1, m-p, p-1, n-p)

for e in matrix:
    print(*e)

