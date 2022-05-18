def dfs(v):
    global num

    if v == b: 
        num = visited.count(True) - 1 # 촌수는 배열의 길이 - 1   --> ex) 나-아빠-할아버지 : 2촌
        return 
    
    for i in matrix[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
            visited[i] = 0 # 이걸 까먹어서 틀린거임
    return 

n = int(input())
a, b = map(int, input().split())
m = int(input())
matrix = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)

num = -1
visited[a] = 1
dfs(a)
print(num)

