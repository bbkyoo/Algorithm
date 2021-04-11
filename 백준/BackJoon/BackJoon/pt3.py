from collections import deque

n = 6
passenger = [1,1,2,3,4]
passenger = [0] + passenger
train = [[1,2],[1,3],[1,4],[1,5]]

matrix = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

for i in range(len(train)):
    matrix[train[i][0]][train[i][1]] = 1
    matrix[train[i][1]][train[i][0]] = 1

def bfs(v):
    q = deque([v])
    visited[v] = 1
    
    while q:
        v = q.popleft()
        
        for i in range(1, n+1):
            if visited[i] == 0 and matrix[v][i]:
                q.append(i)
                visited[i] = 1
                passenger[i] += passenger[v] 
                       
bfs(1)
mx = 0
idx = 0
for i in range(len(passenger)-1,-1,-1):
    if passenger[i] > mx:
        mx = passenger[i]
        idx = i

print("[{},{}]".format(idx,mx))






