import heapq

n, d = map(int, input().split())
arr = [[] for _ in range(10001)]

for _ in range(n):
    start, end, length = map(int, input().split())
    arr[start].append([length, end])

distance = [i for i in range(d+1)]

for i in range(d+1):
    if i != 0:
        distance[i] = min(distance[i], distance[i-1]+1)
    
    for l, e in arr[i]:
        if e <= d and distance[e] > l + distance[i]:
            distance[e] = l + distance[i]

print(distance[d])
