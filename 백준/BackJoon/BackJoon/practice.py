import sys

input = sys.stdin.readline

def rotate_one(matrix):
    return matrix[::-1]

def rotate_two(matrix):
    for i in range(len(matrix)):
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

    return matrix

def rotate_three(matrix):
    global n, m
    n, m = m, n
    copy_matrix = [list(row)[::-1] for row in zip(*matrix)]

    return copy_matrix

def rotate_four(matrix):
    global n, m
    n, m = m, n

    copy_matrix = [list(row) for row in list(zip(*matrix))[::-1]]

    return copy_matrix

def rotate_five(n, m, matrix):
    copy = [[0]*m for _ in range(n)]

    hlaf_n = n // 2
    hlaf_m = m // 2

    for i in range(hlaf_n):
        for j in range(hlaf_n):
            copy[half_n + i][j] = matrix[i][j]

    for i in range(hlaf_n):
        for j in range(hlaf_m, m):
            copy[half_n + i][j] = matrix[i][j]

    for i in range(hlaf_n, n):
        for j in range(hlaf_m, m):
            copy[i][j - half_m] = matrix[i][j]

    for i in range(hlaf_n, n):
        for j in range(hlaf_m):
            copy[i][j - half_m] = matrix[i][j]




n, m, r = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

nums = list(map(int, input().split()))

for num in nums:
    if num == 1:
        matrix = rotate_one(matrix)
    elif num == 2:
        matrix = rotate_two(matrix)
    elif num == 3:
        matrix = rotate_three(matrix)
    elif num == 4:
        matrix = rotate_four(matrix)
    elif num == 5:
        matrix = rotate_five(n, m, matrix)
    else:
        matrix = rotate_six(n, m, matrix)

for i in matrix:
    for j in i:
        print(j, end=" ")
    print()
