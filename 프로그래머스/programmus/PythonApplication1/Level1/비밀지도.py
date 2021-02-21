def solution(n, arr1, arr2):
    mat1 = [[0]*len(arr1) for _ in range(len(arr1))]
    mat2 = [[0]*len(arr2) for _ in range(len(arr2))]
    answer = []

    for i in range(len(arr1)):
        k = len(arr1) - 1
        while arr1[i]:
            mat1[i][k] = arr1[i] % 2
            if arr1[i] // 2 == 1:
                mat1[i][k-1] = 1
                break
            else:
                arr1[i] = arr1[i] // 2 
            k -= 1

    for i in range(len(arr2)):
        k = len(arr2) - 1
        while arr2[i]:
            mat2[i][k] = arr2[i] % 2
        
            if arr2[i] // 2 == 1:
                mat2[i][k-1] = 1
                break
            else:
                arr2[i] = arr2[i] // 2 
            k -= 1

    mat3 = [[0]*len(arr1) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1)):
            mat3[i][j] = mat1[i][j] + mat2[i][j]
            if mat3[i][j] == 2:
                mat3[i][j] = 1
        
            if mat3[i][j] == 1:
                mat3[i][j] = '#'
            else:
                mat3[i][j] = ' '

    for i in range(len(arr1)):
        temp = ''
        for j in mat3[i]:
            temp += j
        answer.append(temp)

    return answer




