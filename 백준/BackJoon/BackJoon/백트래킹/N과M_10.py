import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0]*n
out = []
out_result = []

def dfs(depth, n, m):
    if depth == m:
        temp = ' '.join(map(str, sorted(out)))
        if temp not in out_result:
            out_result.append(temp)
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            out.append(arr[i])
            dfs(depth+1, n, m)
            out.pop()
            visited[i] = 0

dfs(0, n, m)
for i in out_result:
    print(i)


