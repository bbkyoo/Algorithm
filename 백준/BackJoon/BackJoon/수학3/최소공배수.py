# 두 수의 최소공배수 L = lcm(a, b)은 L= lcm(a, b)= a * b / gcd(a, b)이 성립

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int ,input().split())

    temp = 1

    for i in range(1, max(a,b)+1):
        if a % i == 0 and b % i == 0 and temp < i:
            temp = i
    
    result = (a * b) // temp
    print(result)
    