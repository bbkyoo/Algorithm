import sys
sys.setrecursionlimit(10**9)

n = int(input())

matrix = [[] for i in range(n+1)]

for i in range(n-1):
    a,b,c = map(int, input().split())
    matrix[a].append([b,c])
    matrix[b].append([a,c])

result1 = [0 for _ in range(n+1)]

def dfs(start, matrix, result):
    for e, d in matrix[start]:
        if result[e] == 0:
            result[e] = result[start] + d
            dfs(e, matrix, result)

dfs(1, matrix, result1)
result1[1] = 0 # 이거 무조건 해준다.

tmpmax = 0 
index = 0


for i in range(len(result1)):
    if tmpmax < result1[i]:
        tmpmax = result1[i]
        index = i

result2 = [0 for _ in range(n+1)]

dfs(index, matrix, result2)
result2[index] = 0 # 이거 무조건 해준다.
print(max(result2))
