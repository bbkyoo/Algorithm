#M = int(input())
#N = int(input())
#sum = 0
#sosu = []
#min = N

#for i in range(M,N+1):
#    count = 0
#    for j in range(1,N+1,1):
#        if i % j == 0:
#            count += 1
#    if count == 2:
#        sosu.append(i)
#        sum += i
#        if min > i:
#            min = i

# print(sum)
# print(min)

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M = int(input())
N = int(input())

sosu = []

for i in range(M, N+1):
    if isPrime(i):
        sosu.append(i)
        
if len(sosu) == 0:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))











        
