n = int(input())

sum = 0
count_one = 1
count_two = 2
i = 1
result = 0
while True:
    sum += i
    i += sum

    if n % 2 != 0 and count_one == n:
        result = sum    
        break
    
    if n % 2 == 0 and count_two == n:
        result = i    
        break
    
    count_two += 2
    count_one += 2

print(result % 15746)