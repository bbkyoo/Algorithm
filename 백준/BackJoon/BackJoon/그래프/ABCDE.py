# https://kyun2da.github.io/2020/09/21/ABCDE/

def dfs(v, number):
    if number == 4:
        print(1)
        exit()

    for i in matrix[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, number+1)
            visited[i] = 0

n, m = map(int, input().split())
matrix = [[] for _ in range(n)]
visited = [0]*(n)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

for i in range(n):
    visited[i] = 1
    dfs(i, 0)
    visited[i] = 0

print(0)
