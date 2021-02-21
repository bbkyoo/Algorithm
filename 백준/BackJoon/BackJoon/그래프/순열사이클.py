# https://claude-u.tistory.com/434
# 1) 방문 여부 확인용 visited 리스트를 만들어준다.
# 2) 1부터 N까지 숫자를 돌아가면서 해당 숫자의 목적지를 visit해준다.
# 3-1) 방문한 숫자의 다음 숫자도 방문하지 않았다면 visit한다.
# 3-2) 방문했다면 result에 1을 더한 뒤 탈출한다.

import sys
sys.setrecursionlimit(2000)

def dfs(v):
    visited[v] = 1
    next_graph = graph[v]
    if not visited[next_graph]:
        dfs(next_graph)

t = int(input())

for _ in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [1] + [0]*n
    result = 0

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            result += 1
    print(result)