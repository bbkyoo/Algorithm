import sys

input = sys.stdin.readline

def factorial(n):   
    answer = 1
    for i in range(1, n+1):
        answer = answer * i

    return answer

while True:
    num = int(input())

    if num == 0:
        break

    length = len(str(num))

    result = 0
    for i in range(length):
        result += int(str(num)[i]) * factorial(length-i) 

    print(result)