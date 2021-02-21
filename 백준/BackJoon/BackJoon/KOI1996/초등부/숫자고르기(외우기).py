def dfs(v, i):

    visited[v] = 1
    
    for j in arr[v]:
        if visited[j] == 0:
            dfs(j, i)
        elif visited[j] == 1 and j == i:
            result.append(j)

n = int(input())

arr = [[] for _ in range(n+1)]

for i in range(1,n+1):
    arr[i].append(int(input()))

result = []

for i in range(1, n+1):
    visited = [0] * (n+1)
    dfs(i, i)


print(len(result))
for i in result:
    print(i)



