def solution(arr, divisor):
    answer = []
    isTrue = False
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
            isTrue = True

    if isTrue == False:
        answer.append(-1)
    
    answer.sort()
    return answer


     