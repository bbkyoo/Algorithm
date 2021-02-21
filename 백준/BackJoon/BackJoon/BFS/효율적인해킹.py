from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    num = 0
    visited = [0] * (n)
    visited[v] = 1
    
    q = deque()
    q.append(v)

    while q:
        v = q.popleft()
        #num += 1 # 여기에 넣으면 방문한 정점의 수를 셀 수 있다.
        for i in matrix[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                num += 1 # 여기에 넣으면 지난 간선의 수
                
    return num

n, m = map(int, input().split())

matrix = [[] for i in range(n)]

for _ in range(m):
    a, b = map(int ,input().split())
    matrix[b-1].append(a-1) # 이 부분을 조심

ans = [0 for _ in range(n)]

for i in range(n):
    ans[i] = bfs(i)

for i in range(n):
    if ans[i] == max(ans):
        print(i+1, end=' ')


