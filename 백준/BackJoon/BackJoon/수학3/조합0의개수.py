import sys

# 10은 2와 5로 구성되어 있다. 따라서 nCm 내에 있는 2와 5중 최소값이 무엇인지 알아낸뒤 출력하면 된다.

# n!의 5의 개수 세는 함수
def five_count(n):
    answer = 0
    while n != 0:
        n = n//5
        answer += n
    return answer

# n!의 2의 개수 세는 함수
def two_count(n):
    answer = 0
    while n != 0:
        n = n//2
        answer += n
    return answer

n, m = map(int, input().split())

print(min(five_count(n)-five_count(m)-five_count(n-m),two_count(n)-two_count(m)-two_count(n-m)))
