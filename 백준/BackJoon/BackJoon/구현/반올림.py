n = int(input())

for _ in range(n):
    x = list(input())

    if len(x) >= 2:
        for i in range(len(x)-1, 0, -1):
            if int(x[i]) >= 5:
                x[i] = 0
                x[i-1] = int(x[i-1]) + 1
            else:
                x[i] = 0
    
    result = ''
    for i in x:
        result += str(i)

    print(result)

