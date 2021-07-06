# 1. 신장 트리 란?
# 조건
# 본래의 그래프의 모든 노드를 포함해야 함
# 모든 노드가 서로 연결
# 트리의 속성을 만족시킴(사이클이 존재X)

# 2. 최소 신장 트리
# 가능한 신장 트리 중에서, 간선의 가중치 합이 최소인 트리를 저장함

# 3. 크루스칼 알고리즘
# 모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 양 끝의 정점을 비교
# 두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다.

# 4. 유니온 파인드
# 노드 중에 연결된 노드를 찾거나, 노드들을 서로 연결할 때 사용
# 두개의 트리를 하나의 트리로 만들고 사이클을 판단(두 노드가 서로 같은 그래프에 속하(루트노드 보기)는지 판별)한다.

# 5. 유니온 파인드 알고리즘의 고려할 점
# Union은 순서에 따라서 최악의 경우 링크드 리스트와 같은 형태가 될 수 있다
# 이때는 시간복잡도가 O(N)이 될 수 가 있다. 

# union-by-rank, 와 path compression 기법 사용시
# 시간 복잡도가 거의 O(1), 즉 상수에 가깝다고 볼 수 있다. 

# 6. 크루스칼 알고리즘 코드작성

graph = {
    'vertices': ['A','B','C','D','E','F','G'],
    'edges': [
        (7,'A','B'),
        (5,'A','D'),
        (7,'B','A'),
        (9,'B','D'),
        (8,'B','C'),
        (7,'B','E'),
        (8,'C','B'),
        (5,'C','E'),
        (5,'D','A'),
        (9,'D','B'),
        (7,'D','E'),
        (6,'D','F'),
        (5,'E','C'),
        (7,'E','D'),
        (8,'E','F'),
        (6,'F','D'),
        (8,'F','E'),
        (11,'F','G'),
        (9,'G','E'),
        (11,'G','F')
    ]
}

parent = {}
rank = {}

def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2

        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = []

    # 1. 초기화
    for node in graph['vertices']:
        make_set(node)

    # 2. 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    # 3. 간선 연결(사이클 없는)
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    return mst

print(kruskal(graph))

# 7. 시간 복잡도
# 크루스컬 알고리즘의 시간 복잡도는 O(Elog(E))












