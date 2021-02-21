def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5 + 1),1):
            if num % i == 0:
                return False
        return True

M, N = map(int, input().split())

for j in range(M,N+1,1):
    if isPrime(j):
        print(j)