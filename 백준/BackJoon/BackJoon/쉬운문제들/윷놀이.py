# A 도
# B 개
# C 걸
# D 윷
# E 모

a,b,c,d = 0, 0, 0, 0
for i in range(3):
    a,b,c,d = map(int,input().split())
    if ( a + b + c + d ) == 0:
        print("D")
    elif ( a + b + c + d ) == 1:
        print("C")
    elif ( a + b + c + d ) == 2:
        print("B")
    elif ( a + b + c + d ) == 3:
        print("A")
    else:
        print("E")