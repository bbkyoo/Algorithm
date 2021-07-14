from collections import deque
import sys

input = sys.stdin.readline

matrix = [True for _ in range(10001)]

for i in range(2, 101):
    if matrix[i]:
        j = i * 2
        while j < 10001:
            matrix[j] = False
            j += i

def bfs():
    q = deque()
    q.append([a, 0])
    visited = [0 for _ in range(10000)]
    visited[a] = 1

    while q:
        num, cnt = q.popleft()

        if num == b:
            return cnt

        if num < 1000:
            continue

        for i in [1,10,100,1000]:
            n = num - num % (i*10) // i*i
            for j in range(10):
                if visited[n] == 0 and matrix[n]:
                    visited[n] = 1
                    q.append([n, cnt+1])
                n += i

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    result = bfs()
    print(result if result != None else "Impossible")

