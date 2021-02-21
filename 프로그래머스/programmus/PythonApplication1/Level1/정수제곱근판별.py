def solution(n):
    answer = -1

    for i in range(1,n+1):
        if i*i == n:
            answer = i
            break
    
    if answer != -1:
        answer += 1
        answer = answer**2  

    return answer
