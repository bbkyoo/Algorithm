x,y,w,h = map(int, input().split())

if w-1 >= x and y <= h-1:
    if x <= y and x <= w-x and x <= h-y:
        print(x)
    elif y <= x and y <= w-x and y <= h-y:
        print(y)
    elif w-x <= x and w-x <= y and w-x <= h-y:
        print(w-x)
    else:
        print(h-y)