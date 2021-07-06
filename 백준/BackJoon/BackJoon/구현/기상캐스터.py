h, w = map(int, input().split())

matrix = [list(map(str, input())) for _ in range(h)]
visited =[[-1]*w for _ in range(h)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "c":
            visited[i][j] += 1
        elif visited[i][j-1] != -1 and 0 <= j-1:
            visited[i][j] = visited[i][j-1] + 1 

for i in visited:
    for j in i:
        print(j, end=" ")
    print()
     