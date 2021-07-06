from collections import deque

def hospital(city_nodes, city_from, city_to):
    matrix = [[] for _ in range(city_nodes+1)]
    visited = [0]*(city_nodes+1)
    
    for i in range(len(city_from)):
        matrix[city_from[i]].append(city_to[i])
        matrix[city_to[i]].append(city_from[i])
    
    def bfs(v):
        q = deque()
        q.append(v)
        visited[v] = 1
        dist[v] = 1

        while q:
            v = q.popleft()
            
            for i in matrix[v]:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = 1
                    dist[i] = dist[v] + 1

        for i in range(len(dist)):
            if dist[i] > 2:
                visited[i] = 0

    temp = []
    for i in range(1, city_nodes+1):
        temp.append([i, len(matrix[i])])

    temp.sort(key=lambda x : -x[1])
    count = 0 
    for i in range(len(temp)):
        if visited[temp[i][0]] == 0 or len(matrix[temp[i][0]]) >= 3:
            dist = [0]*(city_nodes+1)
            bfs(temp[i][0])
            count += 1

    return count

city_nodes = 7
city_from = [1,3,1,3,2,1]
city_to = [2,6,4,7,5,3]
print(hospital(city_nodes, city_from, city_to))
