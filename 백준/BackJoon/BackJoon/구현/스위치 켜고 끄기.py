n = int(input())
switch = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    gender, num = map(int, input().split()) 
    if gender == 1:
        for i in range(num-1, len(switch),num):
            if switch[i] == 1:
                switch[i] = 0
            elif switch[i] == 0:
                switch[i] = 1

    else:
        num = num -1
        if switch[num] == 1:
            switch[num] = 0
        elif switch[num] == 0:
            switch[num] = 1

        i = 1
        while True: 
            if 0<= num-i and num+i < len(switch):
                if switch[num-i] == switch[num+i]:
                    if switch[num-i] == 1:
                        switch[num-i] = 0
                    elif switch[num-i] == 0:
                        switch[num-i] = 1
                    
                    if switch[num+i] == 1:
                        switch[num+i] = 0
                    elif switch[num+i] == 0:
                        switch[num+i] = 1

                    i += 1
                else:
                    break
            else:
                break

cnt = 0
b = 1
for i in range(len(switch)):
    print(switch[i], end= ' ')
    cnt += 1
    if cnt >= 20*b:
        b += 1
        print()
        








