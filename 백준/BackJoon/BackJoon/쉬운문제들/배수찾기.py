n = int(input())

while True:
    t = int(input())

    if t == 0:
        break

    if t % n == 0:
        print(str(t)+' is a multiple of '+str(n)+'.')
    else:
        print(str(t)+' is NOT a multiple of '+str(n)+'.')