# https://gmlwjd9405.github.io/2018/08/23/algorithm-bipartite-graph.html
# 1. 맨 처음 bfs에 입력한 값은 1로 체크한다
# 2. 그 다음에 이동할 수 있는 지점은 현재 체크한 값에 -1을 곱하면서 이분한다
# 3. 만일 다음에 이동할 지점의 체크값과 현재 체크값이 같으면 이분할 수 없다는 뜻이므로 NO를 출력

from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    q = deque([])
    q.append(v)
    color[v] = 1 

    while q:
        v = q.popleft()    

        for i in matrix[v]:
            if color[i] == 0:
                color[i] = -1 * color[v]
                q.append(i)
            elif color[i] == color[v]:
                return 1
    return 0

k = int(input())

for _ in range(k):
    v, e = map(int,input().split())

    matrix = [[] for i in range(v+1)]   
    color = [0] * (v+1)

    for _ in range(e):
        a, b = map(int, input().split())
        matrix[a].append(b)
        matrix[b].append(a)

    ans = 0
    for i in range(1, v+1):
        if color[i] == 0:
            ans = bfs(i)
            if ans == 1:
                break
    
    if ans == 0:
        print("YES")
    else:
        print("NO")






