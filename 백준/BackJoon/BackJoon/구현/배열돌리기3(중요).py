def rotate_one(matrix): # 상하 반전
    
    return matrix[::-1]

def rotate_two(matrix): # 좌우 반전
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]         

    return matrix

def rotate_three(matrix): # 오른쪽 90도 회전
    global n, m # 이거 무조건 n과 m은 글로벌로 지정
    n,m = m,n
    copy_matrix = [list(row)[::-1] for row in zip(*matrix)] # zip(*matrix) 을 중요하게 알아두기 이 걸 사용하면 [1,2,3] [4,5,6] [7,8,9] 가 [1,4,7] [2,5,8] [3,6,9] 가 된다.

    return copy_matrix     

def rotate_four(matrix): # 왼쪽 90도 회전
    global n, m # 이거 무조건 n과 m은 글로벌로 지정
    n,m = m,n
    copy_matrix = [list(row) for row in list(zip(*matrix))[::-1]] # list(zip(*matrix)) 을 중요하게 알아두기 이 걸 사용하면 [1,2,3] [4,5,6] [7,8,9] 가 [3,6,9] [2,5,8] [1,4,7] 이 된다.

    return copy_matrix     

def rotate_five(n, m, matrix):
    copy = [[0]*m for _ in range(n)]
    
    half_n = n // 2
    half_m = m // 2

    for i in range(half_n):
        for j in range(half_m):
            copy[i][half_m + j] = matrix[i][j]

    for i in range(half_n):
        for j in range(half_m, m):
            copy[half_n + i][j] = matrix[i][j]

    for i in range(half_n, n):
        for j in range(half_m, m):
            copy[i][j - half_m] = matrix[i][j]

    for i in range(half_n, n):
        for j in range(half_m):
            copy[i-half_n][j] = matrix[i][j]

    return copy

def rotate_six(n,m,matrix):
    copy = [[0]*m for _ in range(n)]
    
    half_n = n // 2
    half_m = m // 2

    for i in range(half_n):
        for j in range(half_m):
            copy[half_n+i][j] = matrix[i][j]

    for i in range(half_n, n):
        for j in range(half_m):
            copy[i][j + half_m] = matrix[i][j]

    for i in range(half_n, n):
        for j in range(half_m, m):
            copy[i-half_n][j] = matrix[i][j]

    for i in range(half_n):
        for j in range(half_m, m):
            copy[i][j-half_m] = matrix[i][j]

    return copy

n, m, r = map(int, input().split())

matrix = []
for _ in range(n):
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













