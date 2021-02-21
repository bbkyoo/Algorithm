def solution(x):
    
    arr = []
    temp = x
    while temp:
        arr.append(temp%10)
        temp = temp // 10

    if (x % sum(arr)) == 0:
        answer = True
    else:
        answer = False

    return answer
