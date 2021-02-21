def solution(n):
    arr = []

    while n:
        arr.append(n%10)
        n = n//10
    arr.sort(reverse=True)
    
    answer = ''
    for i in range(len(arr)):
        answer += str(arr[i])

    return int(answer)

