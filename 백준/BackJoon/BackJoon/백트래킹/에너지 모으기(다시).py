import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
maxV = 0

def dfs(depth):
    global maxV

    if len(arr) == 2:
        if depth > maxV:
            maxV = depth
        return

    for i in range(1, len(arr)-1):
        r = arr[i-1] * arr[i+1]
        temp = arr[i]
        del arr[i]
        dfs(depth+r)
        arr.insert(i, temp)

dfs(0)
print(maxV)