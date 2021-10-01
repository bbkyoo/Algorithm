n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
out = []

def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    
    for i in range(n):
        out.append(arr[i])
        solve(depth+1, n, m)
        out.pop()

solve(0, n, m)