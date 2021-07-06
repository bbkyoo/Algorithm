
# https://cotak.tistory.com/66

from collections import deque
from itertools import combinations
import sys

def bfs(same):
    start = same[0]
    q = deque([start])
    visited = set([start])
    _sum = 0

    while q:
        v = q.popleft()
        _sum += people[v]
        for i in matrix[v]:
            if i not in visited and i in same:
                q.append(i)
                visited.add(i)

    return _sum, len(visited)

input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))
matrix = [[] for _ in range(n)]
result = float('inf')

for i in range(n):
    x = list(map(int, input().split()))
    for j in range(1, x[0]+1):
        matrix[i].append(x[j]-1)

for i in range(1, n//2+1):
    combis = list(combinations(range(n) ,i)) 
    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(n) if i not in combi])

        if v1 + v2 == n:
            result = min(result, abs(sum1-sum2))

if result != float('inf'):
    print(result)
else:
    print(-1)






