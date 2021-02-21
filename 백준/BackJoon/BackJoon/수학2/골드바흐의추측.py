def isPrime(num):
    if num == 1 :
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
    return True

T = int(input())

for i in range(T):
    n = int(input())
    for j in range(n//2,1,-1):      # 이 부분을 생각하는게 제일 중요
        if isPrime(j):
            if isPrime(n-j):
                print(j,n-j)
                break


                    
