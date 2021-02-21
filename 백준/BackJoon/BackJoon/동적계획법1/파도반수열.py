T = int(input())

for __ in range(T):
    num = int(input())

    padoban = [1,1,1,2,2]

    if num <= 5:
        print(padoban[num-1])
    else:
        for i in range(5, num):
            padoban.append(padoban[i-1] + padoban[i-5])
        print(padoban[num-1])
        