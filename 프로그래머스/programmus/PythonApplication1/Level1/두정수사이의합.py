def solution(a, b):
    if a > b:
        temp = a
        a = b
        b = temp
    
    answer = 0
    for i in range(a,b+1):
        answer += i
     
    return answer
