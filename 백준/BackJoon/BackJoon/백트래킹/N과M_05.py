n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0]*n
out = []

def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = 1
            out.append(arr[i])
            solve(depth+1, n, m)
            visited[i] = 0
            out.pop()

solve(0, n, m)