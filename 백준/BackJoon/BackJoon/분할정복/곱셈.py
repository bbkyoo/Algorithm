#시간 초과를 해결하기 위해서 곱셈의 개수를 줄이는 분할 정복이 필요하며 아래 과정을 중점적으로 구현하면 된다.

#1. b의 값이 짝수인지 홀수인지 파악한다.
#2. b의 값이 짝수라면 10 ^10 -> (10^5)^2 형태로 바꿔준다.
#3. b의 값이 홀수라면 10 ^11 -> (10^5)^2 * 10 형태로 바꿔준다.

import sys

def power(a,b):
    if b == 1: # b의 값이 1이면 a % C를 return 한다.
        return a % C 
    else:
        temp = power(a, b//2) # a^(b//2)를 미리 구한다.
        if b % 2 == 0:
            return temp * temp % C # b가 짝수인 경우
        else:
            return temp * temp * a % C  # b가 홀수인 경우

A, B, C = map(int, sys.stdin.readline().split())
result = power(A,B)
print(result)