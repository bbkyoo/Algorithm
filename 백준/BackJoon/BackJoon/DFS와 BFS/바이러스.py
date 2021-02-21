import sys

input = sys.stdin.readline

N = int(input()) # 정점의 수
M = int(input()) # 간선의 수
lt = []

matrix = [[0]*(N+1) for i in range(N+1)]
visit_list = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
    
def dfs(V):
    visit_list[V] = 1
    lt.append(V)
    for i in range(1, N+1):
        if( visit_list[i] == 0 and matrix[V][i] == 1):
            dfs(i)
    
dfs(1)
print(len(lt) - 1)