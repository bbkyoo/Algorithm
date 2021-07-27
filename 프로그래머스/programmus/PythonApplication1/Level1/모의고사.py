def solution(answer):
    arr1 = [1,2,3,4,5]
    arr2 = [2,1,2,3,2,4,2,5]
    arr3 = [3,3,1,1,2,2,4,4,5,5]

    result1 = 0
    result2 = 0
    result3 = 0
    for i in range(len(answer)):
        if answer[i] == arr1[i % len(arr1)]:
            result1 += 1
        if answer[i] == arr2[i % len(arr2)]:
            result2 += 1
        if answer[i] == arr3[i % len(arr3)]:
            result3 += 1

    arr = [result1, result2, result3]

    result = []
    
    for i, v in enumerate(arr):
        if v == max(arr):
            result.append(i+1)

    return result