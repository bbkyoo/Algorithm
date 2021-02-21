n = int(input())

sum = 0
count_one = 1
count_two = 2
i = 1
result = 0
while True:
    sum += i

    if n % 2 != 0 and count_one == n:
        result = i    
        break
    
    i += sum
    if n % 2 == 0 and count_two == n:
        result = sum    
        break
    
    count_two += 2
    count_one += 2

print(result)
