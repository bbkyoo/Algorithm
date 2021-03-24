n = int(input())

isTrue = [0,0,0]
real = True

for _ in range(n):
    first, second = map(int, input().split())
    if (first == 1 and second == 3) or (first == 3 and second == 1):
        isTrue[0] += 1
    elif (first == 1 and second == 4) or (first == 4 and second == 1):
        isTrue[1] += 1
    elif (first == 3 and second == 4) or (first == 4 and second == 3):
        isTrue[2] += 1
    else:       
        real = False

if (real == False) or (0 in isTrue):
    print("Woof-meow-tweet-squeek")
else:
    print("Wa-pa-pa-pa-pa-pa-pow!")
    
