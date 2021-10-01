import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
out = []
visited = [0]*n
out_result = []

def solve(depth, n, m):
    if depth == m:
        if ' '.join(map(str, sorted(out))) not in out_result:
            out_result.append(' '.join(map(str, sorted(out))))
            print(' '.join(map(str, sorted(out))))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            out.append(arr[i])
            solve(depth+1, n, m)
            visited[i] = 0
            out.pop()

solve(0, n, m)