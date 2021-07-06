# 1. 프림 알고리즘
# 시작 정점을 선택한 후, 정점에 인접한 간선중 최소 간선으로 연결된 정점을 선택하고
# 해당 정점에서 다시 최소 간선으로 연결된 정점을 선택하는 방식으로 최소 신장 트리를 확장해나가는 방식

# 2. 프림 알고리즘 코드 작성

from heapq import *
from collections import defaultdict

edges = [
    (7, 'A', 'B'),
    (5, 'A', 'D'),
    (8, 'B', 'C'),
    (9, 'B', 'D'),
    (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'),
    (6, 'D', 'F'),
    (8, 'E', 'F'),
    (9, 'E', 'G'),
    (11, 'F', 'G')
]

def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)

    return mst

print(prim('A', edges))

# 3. 시간 복잡도
# 최악의 경우 O(Elog(E))시간 복잡도를 가짐 



