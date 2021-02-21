N = int(input())
sum = 0

for i in range(N+1 ,N**2,N+1):
    if i // N == i % N:
        sum += i

print(sum)