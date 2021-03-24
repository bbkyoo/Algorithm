n, m = map(int, input().split())

matrix = [100*[0] for _ in range(100)]

for _ in range(n):
    l_x, l_y, r_x, r_y = map(int, input().split())

    for i in range(l_x-1, r_x):
        for j in range(l_y-1, r_y):
            matrix[i][j] += 1
cnt = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > m:
            cnt += 1

print(cnt)
