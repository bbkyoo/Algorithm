# 1. 최단 경로란?
# 두 노드를 잇는 가장 짧은 경로를 찾는 문제
# 가중치 그래프 에서 간선의 가중치 합이 최소가 되도록 하는 경로를 찾는 것이 목적

# 문제종류
# - 단일 출발 및 단일 도착
#   : 그래프 내의 특정 노드 u에서 출발, 또다른 특정 노드 v에 도착하는 가장 짧은 경로 찾기
# - 단일 출발 최단 경로 문제
#   : 그래프 내에 특정 노드 u와 그래프 내 다른 모든 노드 각각의 가장 짧은 경로를 찾는 문제  
# - 전체 쌍 최단 경로
#   : 그래프 내의 모든 노드 쌍(u, v)에 대한 최단 경로를 찾는 문제    

# 2. 다익스트라 알고리즘 구현

# heapq 라이브러리를 활용하여 우선순위 큐 구현

import heapq

q = []
heapq.heappush(q, [2, 'A'])
heapq.heappush(q, [5, 'B'])
heapq.heappush(q, [1, 'C'])
heapq.heappush(q, [7, 'D'])
print(q)

for i in range(len(q)):
    print(heapq.heappop(q))

# 다익스트라 구현

mygraph = {
    'A': {'B':8, 'C':1, 'D':2},
    'B': {},
    'C': {'B':5, 'D':2},
    'D': {'E':3, 'F':5},
    'E': {'F':1},
    'F': {'A':5}
}

def dijkstra(graph, start):
    distances = {node:float('inf') for node in graph}
    distances[start] = 0
    q = []

    heapq.heappush(q, [distances[start], start])

    while q:
        current_distance, current_node = heapq.heappop(q)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(q, [distance, adjacent])

    return distances

print(dijkstra(mygraph,'A'))

# 3. 시간 복잡도
# 과정1: 각 노드마다 인접한 간선들을 모두 검사하는 과정
#       - O(E) 시간이 걸림 E는 간선의 약자 

# 과정2: 우선순위 큐에 노드/거리 정보를 넣고 삭제(pop)하는 과정
#       - 각 간선마다 최대 한 번 일어날 수 있으므로, 최대 O(E)의 시간이 걸리고
#       - O(E)개의 노드/거리 정보에 대해 우선순위 큐를 유지하는 작업은 O(log(E))가 걸림
#       - o(log(E)) 시간이 걸림

# 총 시간 복잡도 : O(Elog(E))









