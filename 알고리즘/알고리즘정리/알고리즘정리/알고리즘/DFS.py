# 1. BFS, DFS
# BFS: 정점들과 같은 레벨에 있는 노드들을 먼저 탐색하는 방식
# DFS: 정점의 자식들을 먼저 탐색하는 방식

# 2. 구현

def dfs(graph, start_node):
    visited = []
    need_visit = []

    need_visit.append(start_node)    

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

# 3. 시간복잡도
# 노드 수: V
# 간선 수: E
# O(V+E)


