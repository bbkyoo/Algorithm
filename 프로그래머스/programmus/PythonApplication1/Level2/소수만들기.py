from itertools import combinations

def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    temp = list(combinations(nums,3))

    count = 0
    for i in range(len(temp)):
        test = sum(temp[i])
        if isPrime(test):
            count += 1

    return count

