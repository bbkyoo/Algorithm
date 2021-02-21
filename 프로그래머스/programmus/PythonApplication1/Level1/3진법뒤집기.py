def solution(n):
    
    three = []
    while n > 0:
        three.append(n % 3)
        n = n//3

    three.reverse()
    answer = 0

    for i in range(len(three)):
        answer += (three[i] * (3**i))
    
    return answer


       