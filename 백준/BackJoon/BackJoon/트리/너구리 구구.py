def dfs(v, p):
    ret = 0
    for i in matrix[v]:
        if i[0] == p:
            continue
        ret = max(ret, dfs(i[0], v) +i[1])

    return ret

n = int(input())

matrix = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    matrix[a].append([b,c])
    matrix[b].append([a,c])

print(matrix)
print(dfs(1, -1))






