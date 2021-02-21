import sys

input = sys.stdin.readline

def isPrime(num):
    if num == 1:
        return False

    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            return False
    return True

n = int(input())

number = []

for i in range(1,n+1):
    if isPrime(i):
        number.append(i)

sum = 0
end = 0
count = 0

for start in range(len(number)):
    while end < len(number) and sum < n:
        sum += number[end]
        end += 1

    if sum == n:
        count += 1

    sum -= number[start]

print(count)