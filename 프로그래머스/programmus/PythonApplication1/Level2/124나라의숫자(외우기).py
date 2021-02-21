# 이 문제는 삼진법 문제이다 이 삼진법 문제라는 것을 파악하고 아래 while문을 유심하게 보자 
# 그리고 이 문제랑 코드 외우기

def solution(n):

    answer = ''
    while n > 0:
        n -= 1
        answer = '124' [n%3] + answer # '124' [n%3] 이 코드를 기억하고 유용하게 쓰자 
        n //= 3

    return answer





