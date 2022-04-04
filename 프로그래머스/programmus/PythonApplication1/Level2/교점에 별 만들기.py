def solution(line):
    arr = []

    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if line[i][0] * line[j][1] - line[i][1] * line[j][0] != 0:
                x = (line[i][1] * line[j][2] - line[i][2] * line[j][1]) / (
                            line[i][0] * line[j][1] - line[i][1] * line[j][0])
                y = (line[i][2] * line[j][0] - line[i][0] * line[j][2]) / (
                            line[i][0] * line[j][1] - line[i][1] * line[j][0])
                if x == int(x) and y == int(y):
                    arr.append([int(x), int(y)])

    min_x = sorted(arr, key=lambda x: x[0])[0][0]
    max_x = sorted(arr, key=lambda x: x[0])[-1][0]
    min_y = sorted(arr, key=lambda x: x[1])[0][1]
    max_y = sorted(arr, key=lambda x: x[1])[-1][1]

    matrix = []

    for i in range(min_y, max_y + 1):
        line = []
        for j in range(min_x, max_x + 1):
            line.append('.')
        matrix.append(line)

    ####################### 이걸 몰라서...
    for i in arr:
        a, b = i
        x, y = abs(max_y - b), abs(min_x - a)
        matrix[x][y] = '*'
    #####################################

    result = []
    for i in matrix:
        temp = ''
        for j in i:
            temp += j
        result.append(temp)
    return result