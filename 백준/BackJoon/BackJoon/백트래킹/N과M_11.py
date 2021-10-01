import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
out = []
out_result = []

def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return

    overlap = 0
    for i in range(n):
        if overlap != arr[i]:
            out.append(arr[i])
            overlap = arr[i]
            dfs(depth+1, n, m)
            out.pop()

dfs(0, n, m)
