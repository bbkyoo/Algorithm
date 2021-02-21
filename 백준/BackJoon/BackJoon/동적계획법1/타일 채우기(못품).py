# 점화식 d[n] = 3 * d[n-2] + 2 * d[n-4] ~~~ 2 * d[0]

n = int(input())

def solve(n):
    if n == 1:
        return 0
    if n == 2:
        return 3
    