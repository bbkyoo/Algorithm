from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 0

    while q:
        v = q.popleft()

        if v == b:
            return visited[v]

        for i in matrix[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                q.append(i)

    return -1

a, b = map(int, input().split())
n, m = map(int, input().split())

matrix = [[] for _ in range(n+1)]
visited = [-1]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)

print(bfs(a))




# 다익스트라 풀이
#import sys, heapq
#MAX = int(1e9)
#a,b = map(int,sys.stdin.readline().split())
#n,m = map(int,sys.stdin.readline().split())

#board = [[] for _ in range(n+1)]
#for _ in range(m):
#    x,y = map(int,sys.stdin.readline().split())
#    board[x].append(y)
#    board[y].append(x)

#dist_arr = [MAX]*(n+1)
#dist_arr[a]=0
#q = []
#heapq.heappush(q, (0,a))
#while q:
#    dist, cur = heapq.heappop(q)
#    if dist_arr[cur] < dist:
#        continue

#    for next in board[cur]:
#        if dist_arr[next] > dist+1:
#            dist_arr[next] = dist+1
#            heapq.heappush(q, (dist+1,next))

#if dist_arr[b] == MAX:
#    print(-1)
#else:
#    print(dist_arr[b])