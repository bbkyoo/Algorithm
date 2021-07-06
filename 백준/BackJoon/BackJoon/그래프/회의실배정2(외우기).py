import sys

input = sys.stdin.readline

def dfs(n,val):
    global res
    
    if n >= N and res < val:
        res = val
        return

    for i in range(n, N):
        dfs(i+2, val+arr[i][2])

N = int(input())

arr = []
for _ in range(N):
    s, e, number = map(int, input().split())
    arr.append([s,e,number])
    
arr.sort()
res = 0
dfs(0,0)
print(res)