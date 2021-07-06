# 1. BFS, DFS
# BFS: 정점들과 같은 레벨에 있는 노드들을 먼저 탐색하는 방식
# DFS: 정점의 자식들을 먼저 탐색하는 방식

def bfs(graph, start_node):
    visited = []
    need_visit = []

    need_visit.append(start_node)
    count = 0 # 간선의 수
    while need_visit:
        count += 1
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    print(count)
    return visited

# 2. 시간 복잡도
# 노드 수: V
# 간선 수: E
# 시간 복잡도: O(V+E)







