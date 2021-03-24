def fivonach(n):    
    a,b = 1, 1
    if n == 1 or n == 2:
        return 1

    for i in range(1, n):
        a, b = b, a+b

    return a

n = int(input())
length = list(map(int, input()))

cnt = length.count(1)
count = 1

if cnt == len(length):
    count = fivonach(n)
    print(count)
    
else:
    temp = 0
    mul = []
    for i in range(len(length)):
        if length[i] == 1:
            temp += 1
        elif length[i] == 0:
            mul.append(fivonach(temp))
            temp = 0
    mul.append(fivonach(temp))

    for i in mul:
        if i != 0:
            count *= i
           
    print(count)
    















