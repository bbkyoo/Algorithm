from collections import deque

def bfs(x, y):
    q, c = deque(), []
    q.append([x, y, 20])
    c.append([x, y, 20])
    while q:
        x, y, beer = q.popleft()
        if x == rock_x and y == rock_y:
            print("happy")
            return
        for nx, ny in matrix:
            if [nx, ny, 20] not in c:
                temp = abs(nx-x) + abs(ny-y)
                if beer*50 >= temp:
                    q.append([nx, ny, 20])
                    c.append([nx, ny, 20])
    print("sad")
    return

t = int(input())

for _ in range(t):
    n = int(input())
    
    matrix = []
       
    home_x , home_y = map(int, input().split())

    for _ in range(n):
        x, y = map(int, input().split())
        matrix.append([x, y])

    rock_x, rock_y = map(int, input().split())
    matrix.append([rock_x, rock_y])
    bfs(home_x , home_y)

