while True:
    a,b,c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    if (b - a) == (c - b):
        print('AP ' + str(2*c -b))
    else:
        print('GP ' + str(c*(b//a)))
        
