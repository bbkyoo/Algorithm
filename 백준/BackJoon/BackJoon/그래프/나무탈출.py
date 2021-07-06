# https://m.blog.naver.com/PostView.naver?blogId=pyl970&logNo=221460164127&proxyReferer=https:%2F%2Fwww.google.com%2F
# 리프노드의 레벨들의 합이 짝수면 먼저 한 사람(성원)이 무조건 지고,
# 홀수면 먼저 한 사람(성원)이 이기게 된다.

from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    global result

    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        notleaf = False
        v = q.popleft()

        for i in matrix[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                notleaf = True
                q.append(i)

        if notleaf == False:
            result = result + visited[v] - 1

n = int(input())
result = 0

matrix = [[] for _ in range(n+1)]
visited = [0] * (n+1) 

for _ in range(n-1):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

bfs(1)

if result % 2 == 1:
    print("Yes")
else:
    print("No")