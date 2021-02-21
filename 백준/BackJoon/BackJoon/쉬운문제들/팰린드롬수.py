while True:
    N = int(input())
    if N == 0:
        break
    
    lst = []
    while True:
        if N == 0:
            break
        lst.append(N % 10)
        N = N // 10

    if len(lst) % 2 == 0:
        count = 0
        num = len(lst)
        for i in range(1,(num // 2)+1):
            if lst[(num//2)-i] == lst[(num//2)+i-1]:
                count += 1
   
        if count == num//2:
            print("yes")
        else:
            print("no")

    else:
        count = 0
        num = len(lst)
        for i in range(1, (num // 2) + 1):
            if lst[(num//2)-i] == lst[(num//2)+i]:
                count += 1

        if count == num//2:
            print("yes")
        else:
            print("no")