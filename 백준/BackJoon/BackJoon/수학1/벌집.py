N = int(input())

count = 1

while N > 1:
    N = N - (6*count)
    count += 1

print(count)