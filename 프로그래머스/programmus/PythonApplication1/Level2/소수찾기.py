from itertools import permutations

def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)

    arr = set()
    for i in range(len(numbers)):
        temp = list(set(map(''.join , permutations(numbers, i+1)))) # map함수를 사용해서 더 간단하게 permutations을 가공한다.
        for i in temp:
            if isPrime(int(i)):
                arr.add(int(i))

    return len(arr)