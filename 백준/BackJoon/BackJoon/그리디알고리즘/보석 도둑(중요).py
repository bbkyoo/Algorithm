# https://claude-u.tistory.com/343

import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = []

for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(arr,[m,v])

c = []

for _ in range(k):
    heapq.heappush(c, int(input()))

result = 0
capable_gem = []

for i in range(k):
    top = heapq.heappop(c)

    while arr and top >= arr[0][0]:
        [m, v] = heapq.heappop(arr)
        heapq.heappush(capable_gem, -v)
    
    if capable_gem:
        result -= heapq.heappop(capable_gem)
    elif not arr:
        break

print(result)