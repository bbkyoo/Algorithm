# 처음 시작점 N에서 갈 수 있는 점 N*2, N+1, N-1 세 점에서 또 각점이 갈 수 있는 세 점씩을 계속 탐색해서 K와 같을 때를 찾으면 된다. 
# 단, count를 +1 해주는 위치와 사용하는 방법이 중요한데, 
# count를 방문 안했을시 방문 할 때마다 +1 해주면 다른 탐색도 거쳐와서 N == K 일때도 생길 수 있기 때문에 count 값이 크게 나온다. 
# 때문에 e라는 점이 큐에 몇번째로 들어갔는지 판단후 +1 해주기 위해 count를 q에 같이 넣어줌으로써 해결했다.

from collections import deque
import sys

#input = sys.stdin.readline

#def bfs(v):
#    count = 0
#    q = deque([[v,count]])
    
#    while q:
#        v = q.popleft()
#        e = v[0]
#        count = v[1]
#        if not visited[e]:
#            visited[e] = True
#            if e == k:
#                return count
#            count += 1
#            if (e * 2) <= 100000:
#                q.append([e*2 , count])
#            if (e + 1) <= 100000:
#                q.append([e+1, count])
#            if (e - 1) >= 0:
#                q.append([e-1, count])
#    return count # 이거에 대해 생각을 많이 해봤는데 n = 0 일때를 생각해보면 바로 이 것이 있는 이유가 나온다. 

#n, k = map(int, input().split())

#visited = [False] * 100001

#print(bfs(n))
# https://it-garden.tistory.com/183

def bfs(n, k):
    q = deque()
    q.append(n)
    
    visited = [0] * 100001

    while q:
        x = q.popleft()

        if x == k:
            return visited[x]

        for i in (x-1, x+1, x*2):
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)

n, k = map(int, input().split())

print(bfs(n,k))


























