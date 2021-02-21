# 어떤 수 N (1 ≤ N ≤ 1,000,000)이 주어졌을 때, N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수를 구하는 프로그램을 작성하시오.

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5 + 1), 1):
            if num % i == 0:
                return False
        return True

def pallindrom(num):
    nums = []
    while num:
        nums.append(num%10)
        num = num // 10
    
    nums_go = nums
    nums = list(reversed(nums))
    
    if nums_go == nums:
        return True
    return False

n = int(input())

for i in range(n , 2147483647 ,1):
    if (isPrime(i) and pallindrom(i)):
        print(i)
        break
