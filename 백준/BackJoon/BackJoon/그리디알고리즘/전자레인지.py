# A 300초
# B 60초
# C 10초

T = int(input())

a,b,c = 0,0,0

while T != 0 :
    if T < 0:
        break
    
    if T >= 300:
        a += 1
        T -= 300
    elif T < 300 and T >= 60:
        b += 1
        T -= 60
    else:
        c += 1
        T -= 10

if T < 0:
    print(-1)
else:
    print(a, b, c)