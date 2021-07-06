def dfs(count, x, y):
    if count == N:
        return 1

    matrix[x][y] = 1
    result = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if matrix[nx][ny]:
            continue

        result += dfs(count+1, nx, ny)*percent[i]
    matrix[x][y] = 0
    return result

N, e, w, s, n = map(int, input().split())

percent = [e/100, w/100, s/100, n/100]
matrix = [[0 for _ in range(2*N+1)] for __ in range(2*N+1)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(dfs(0,N,N))
