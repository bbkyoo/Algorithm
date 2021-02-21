N = int(input())

count = 0
k = 1
while True:
    if N < k:
        k = 1
    N -= k
    count += 1    
    k += 1
    if N <= 0:
        break


print(count)