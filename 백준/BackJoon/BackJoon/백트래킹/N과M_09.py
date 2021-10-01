n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0]*n
out = []
all_out = []

def solve(depth, n, m):
    if depth == m:
        temp = ' '.join(map(str, out))
        if temp not in all_out:
            all_out.append(temp)
        return

    for i in range(n):
        if visited[i] == 0:
            out.append(arr[i])
            visited[i] = 1
            solve(depth+1, n, m)
            visited[i] = 0
            out.pop()

solve(0, n, m)
for i in all_out:
    print(i)