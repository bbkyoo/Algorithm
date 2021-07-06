# https://welog.tistory.com/48

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

def dfs(bomb):
    global n, result

    while bomb:
        x, y = bomb.pop()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx == 0 or nx == n-1) or (ny == 0 or ny == n-1):
                if matrix[nx][ny] == 0:
                    break

        else:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if (nx == 0 or nx == n-1) or (ny == 0 or ny == n-1):
                    matrix[nx][ny] -= 1
            result += 1
    return

n = int(input())

result = 0
matrix = []
bomb = []
for _ in range(n):
    matrix.append(list(input()))

if n > 4:
    result += (n-4)**2

for i in range(n):
    for j in range(n):
        if i == 1 or i == n-2:
            if matrix[i][j] == '#':
                bomb.append([i, j])
            else:
                matrix[i][j] = int(matrix[i][j])

        elif 1 < i < n-2:
            if j == 1 or j == n-2:
                bomb.append([i, j])
            else:
                if matrix[i][j] != '#':
                    matrix[i][j] = int(matrix[i][j])
              
        else:
            if matrix[i][j] != '#':
                matrix[i][j] = int(matrix[i][j])
            
dfs(bomb)
print(result)
                    