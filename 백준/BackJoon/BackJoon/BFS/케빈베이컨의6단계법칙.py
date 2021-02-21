# BOJ의 유저가 5명이고, 1과 3, 1과 4, 2와 3, 3과 4, 4와 5가 친구인 경우를 생각해보자
# 1은 2까지 3을 통해 2단계 만에, 3까지 1단계, 4까지 1단계, 5까지 4를 통해서 2단계 만에 알 수 있다. 따라서, 케빈 베이컨의 수는 2+1+1+2 = 6이다.
from collections import deque
import sys

input = sys.stdin.readline

def bfs(start):
    q = deque()
    visited[start] = 1
    q.append((start, 0)) # 노드, depth
    kevin_num = 0

    while q:
        x, depth = q.popleft() 
        for i in matrix[x]:
            if visited[i] == 0:
                visited[i] = 1
                q.append((i, depth+1))
                kevin_num += depth+1

    global answer, result
    if (result > kevin_num):
        result = kevin_num
        answer = start

n, m = map(int, input().split())
result = 100000000
matrix = [[] for _ in range(n+1)]
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

for i in range(1, n+1):
    visited = [0] * (n+1)    
    bfs(i)
    
print(answer)