def solution(n, arr1, arr2):
    def trans(num):
        nonlocal n
        answer = []
        while num != 0:
            answer.append(num%2)
            num //= 2

        if len(answer) < n:
            for i in range(len(answer),n):
                answer.append(0)

        answer.reverse()
        return answer

    matrix1 = []
    matrix2 = []
    matrix = []
    for i in range(n):
        matrix1.append(trans(arr1[i]))
        matrix2.append(trans(arr2[i]))


    for i in range(n):
        line = ''
        for j in range(n):
            if matrix1[i][j] == 1 or matrix2[i][j] == 1:
                line += '#'
            else:
                line += ' '
        matrix.append(line)

    return matrix






