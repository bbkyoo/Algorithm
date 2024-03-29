import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
inDegree = [0 for _ in range(32001)]
graph = [[] for _ in range(32001)]
q = deque()

for _ in range(m):
    a, b = map(int, input().split()) 
    inDegree[b] += 1
    graph[a].append(b)

for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)

while q:
    student = q.popleft()
    # inDegree가 0인 정점을 제거하고, 해당 정점이 참조하고있던 점들의 inDegree를 감소시킨다.
    for j in graph[student]:
        inDegree[j] -= 1
        if inDegree[j] == 0:
            q.append(j)
    print(student, end= ' ')

        