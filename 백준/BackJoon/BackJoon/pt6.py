n, m = map(int, input().split())

matrix = []
for i in range(m):
    matrix.append(list(map(int, input().split())))

if n == 1 and m == 1:
    print(matrix[0])
elif n == 1:
    result = 0
    for i in matrix:
        for j in i:
            result += j
    print(result)
elif m == 1:
    print(sum(matrix))
else:
    for i in range(1,n):
        matrix[0][i] += matrix[0][i-1]

    for i in range(1,m):
        matrix[i][0] += matrix[i-1][0]

    for i in range(1,m):
        for j in range(1,n):
            matrix[i][j] += max(matrix[i-1][j], matrix[i][j-1])
    
    print(matrix[-1][-1])
                
        