import sys

input = sys.stdin.readline 

def go(x, y):
    global dp

    if y <= 0:
        return 1

    ret = dp[x][y]
    if ret != -1:
        return ret

    ret = 0
    for u in v[x]:
        ret = (ret + go(u, y-1)) % mod

    return ret

def solve():
    n = int(input())

    sum = 0

    for i in range(10):
        sum = (sum + go(i, n-1)) % mod

    print(sum)

t = int(input())

v = [
[7],
[2,4],
[1,3,5],
[2,6],
[1,5,7],
[2,4,6,8],
[3,5,9],
[0,4,8],
[5,7,9],
[6,8]
]
 
mod = 1234567

for _ in range(t):
    dp = [[-1]*(1001) for _ in range(10)]
    solve()
    

    