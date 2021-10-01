import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
out = []

def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return

    for i in range(n):
        if depth == 0 or out[depth-1] <= arr[i]:
            out.append(arr[i])
            solve(depth+1, n, m)
            out.pop()

solve(0, n, m)