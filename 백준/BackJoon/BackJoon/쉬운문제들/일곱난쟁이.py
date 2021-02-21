import random

tall = [int(input()) for __ in range(9)]

while True:
    result = 0
    lst = random.sample(tall,7)

    result = sum(lst)
    
    if result == 100:
        lst.sort()
        for i in lst:
            print(i)
        break
    else:
        continue