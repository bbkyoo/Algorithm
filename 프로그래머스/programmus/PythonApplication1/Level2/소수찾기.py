from itertools import permutations

def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers) 
    answer = []

    for i in range(1,len(numbers)+1):
        temp = list(map(''.join, permutations(numbers, i)))
        answer += temp
    answer = list(set(answer))

    result = []
    for i in range(len(answer)):
        if answer[i][0] != '0':
            result.append(answer[i])

    result = list(map(int, result))

    count = 0
    for i in range(len(result)):
        if result[i] != 1:
            if isPrime(result[i]):
                count += 1

    return count

