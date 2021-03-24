import copy

n = int(input())

board = []
for _ in range(n):
    board.append(list(input()))

def switch(arr):
    c_count = 0
    p_count = 0
    z_count = 0
    y_count = 0

    for i in range(len(arr)):
        c_c = 0
        p_c = 0
        z_c = 0
        y_c = 0
        for j in range(len(arr[i])):
            if arr[i][j] == 'C':
                c_c += 1
            else:
                c_count = max(c_count, c_c)
                c_c = 0

            if arr[i][j] == 'P':
                p_c += 1
            else:
                p_count = max(p_count, p_c)
                p_c = 0

            if arr[i][j] == 'Z':
                z_c += 1
            else:
                z_count = max(z_count, z_c)
                z_c = 0

            if arr[i][j] == 'Y':
                y_c += 1
            else:
                y_count = max(y_count, y_c)
                y_c = 0 
        
        c_count = max(c_count, c_c)
        p_count = max(p_count, p_c)
        z_count = max(z_count, z_c)
        y_count = max(y_count, y_c)


    for i in range(len(arr)):
        c_c = 0
        p_c = 0
        z_c = 0
        y_c = 0
        for j in range(len(arr[i])):
            if arr[j][i] == 'C':
                c_c += 1
            else:
                c_count = max(c_count, c_c)
                c_c = 0

            if arr[j][i] == 'P':
                p_c += 1
            else:
                p_count = max(p_count, p_c)
                p_c = 0

            if arr[j][i] == 'Z':
                z_c += 1
            else:
                z_count = max(z_count, z_c)
                z_c = 0

            if arr[j][i] == 'Y':
                y_c += 1
            else:
                y_count = max(y_count, y_c)
                y_c = 0

        c_count = max(c_count, c_c)
        p_count = max(p_count, p_c)
        z_count = max(z_count, z_c)
        y_count = max(y_count, y_c)

    result = max(c_count, p_count,z_count, y_count)

    return result

answer = switch(board)
for i in range(n):
    for j in range(1, n):
        temp = copy.deepcopy(board)
        temp[i][j-1], temp[i][j] = temp[i][j], temp[i][j-1]
        answer = max(answer, switch(temp))

for i in range(n):
    for j in range(1, n):
        temp = copy.deepcopy(board)
        temp[j-1][i], temp[j][i] = temp[j][i], temp[j-1][i]
        answer = max(answer, switch(temp))

print(answer)

















