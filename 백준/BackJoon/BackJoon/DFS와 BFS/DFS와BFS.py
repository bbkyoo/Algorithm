# DFS : 이어달리기, 바통터치 느낌 (한 정점에서 이어진 다른 정점 간 다음, 그 정점과 이어진 정점 순차적으로 이어주기)
# BFS : 와이파이 느낌 (우선 한 정점과 이어진 모든 정점을 들른 후, 다음 정점도 마찬가지로 시작)
# dfs의 경우 : 1에서 시작해서 이어져있는 2로 간후, 2와 이어져있는 4로 가고, 4와 이어져있는 3으로 감 (바통터치)
# bfs의 경우 : 1(공유기)에서 시작해서 이어져있는 2로 간후, 3도 가고난 후, 2(공유기)와 이어진 4로 간 후, 3(공유기)과 이어진 4로 감

from collections import deque
import sys

input = sys.stdin.readline
N, M, V = map(int, input().split())

matrix = [[0]*(N+1) for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

visit_list = [0]*(N+1)

def dfs(V):
    visit_list[V] = 1 # 방문한 점 1로 표시
    print(V, end=' ')
    for i in range(1, N+1):
        if(visit_list[i] == 0 and matrix[V][i] == 1):
            dfs(i)

def bfs(V):
    queue = deque([V]) # 들려야 할 정점 저장
    visit_list[V] = 0 # 방문한 점 0으로 표시
    while queue:
        V = queue.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit_list[i] == 1 and matrix[V][i] == 1):
                queue.append(i)
                visit_list[i] = 0

dfs(V)
print()
bfs(V)