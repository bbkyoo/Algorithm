n = int(input())
s = [0]*n
w = [0]*n
for i in range(n):
    s[i], w[i] = map(int, input().split())
    
res = 0
def solve(depth, eggs):
    global res
    if depth == n:
        cnt = 0
        for i in range(n):
            if eggs[i] <= 0:
                cnt += 1
        res = max(res, cnt)
        return

    if eggs[depth] > 0:
        for i in range(n):
            flag = False
            if eggs[i] > 0 and i != depth:
                flag = True
                tmp = eggs.copy()
                tmp[i] -= w[depth]
                tmp[depth] -= w[i]
                solve(depth+1, tmp)
        if not flag:
            solve(depth+1, eggs)
    else:
        solve(depth+1, eggs)

solve(0, s)
print(res)