from collections import defaultdict, deque

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

def bfs1(v):
    q = deque([])
    q2 = deque([])
    ship = 1
    wolf = 0
    q.append([ship, wolf, v])
    mx = ship
    temp = []
    while q:
        v = q.popleft()
        temp_ship = v[0]
        temp_wolf = v[1]
        for i in matrix[v[2]]:
            if info[i] == 0:
                temp_ship += 1
            elif info[i] == 1:
                temp_wolf += 1

            if temp_ship > temp_wolf:
                q.append([temp_ship, temp_wolf, i])
                if temp_ship > mx:
                    q2.append(temp_ship, temp_wolf, i)
                    mx = max(mx, temp_ship) 

            else:
                q2.append([temp_ship,temp_wolf,i])
                temp_wolf -= 1
    return mx

def bfs2(v):
    ship = 1
    wolf = 0
    q.append([ship, wolf, v])
    mx = ship
    temp = []
    while q:
        v = q.popleft()
        temp_ship = v[0]
        temp_wolf = v[1]
        for i in matrix[v[2]]:
            if info[i] == 0:
                temp_ship += 1
            elif info[i] == 1:
                temp_wolf += 1

            if temp_ship > temp_wolf:
                q.append([temp_ship, temp_wolf, i])
                if temp_ship > mx:
                    temp = [temp_ship, temp_wolf, i]
                mx = max(mx, temp_ship) 

            else:
                q2.append([temp_ship,temp_wolf,i])
                temp_wolf -= 1

matrix = defaultdict(list)

for i in edges:
    matrix[i[0]].append(i[1])

print(root(0))
