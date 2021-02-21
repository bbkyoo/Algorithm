def solution(arr):
    
    answer = []
    if len(arr) == 0:
        return answer

    answer = [arr[0]]
    k = 0
    for i in range(1,len(arr)):
        if arr[i] != answer[k]:
            answer.append(arr[i])
            k += 1
    return answer

    