from heapq import heappush, heappop
import sys

input = sys.stdin.readline

def dijkstra(v):
    heap = []
    heappush(heap, [0, v])
    dp = [1000000000 for i in range(n + 1)]
    dp[v] = 0

    while heap:
        wei, num = heappop(heap)
        for next_num, next_wei in matrix[num]:
            weight = wei + next_wei   
            if dp[next_num] > weight:
                dp[next_num] = weight
                heappush(heap, [weight, next_num])
                    
    return dp    
    
n, m = map(int, input().split())

matrix = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a].append([b,1])
    matrix[b].append([a,1])

dp = dijkstra(1) 
max_dp = max(dp[1:])
print(dp.index(max_dp), max_dp, dp.count(max_dp))
















