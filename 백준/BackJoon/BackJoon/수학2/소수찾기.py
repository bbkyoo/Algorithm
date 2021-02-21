n = int(input())
ns = list(map(int, input().split(' ')))

sosu = 0

if len(ns) == n:
    for i in ns:
        count = 0
        for j in range(1,i+1,1):
            if (i % j == 0):
                count += 1
        if count == 2:
            sosu += 1

print(sosu)    
    