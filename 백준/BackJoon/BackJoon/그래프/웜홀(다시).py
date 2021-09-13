import sys
input = sys.stdin.readline

def bellmanFord():
    global isPossible
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            for wei, vec in adjList[j]:
                if dist[vec] > wei + dist[j]:
                    dist[vec] = wei + dist[j]
                    if i == n:
                        isPossible = False

tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())

    inf = sys.maxsize

    dist = [inf for _ in range(n+1)]

    adjList = [[] for _ in range(n+1)]

    for _ in range(m):
        s, e, t = map(int, input().split())
        adjList[s].append([t, e])
        adjList[e].append([t, s])

    for _ in range(w):
        s, e, t = map(int, input().split())
        adjList[s].append([-t, e])

    isPossible = True
    bellmanFord()

    print("NO" if isPossible else "YES")