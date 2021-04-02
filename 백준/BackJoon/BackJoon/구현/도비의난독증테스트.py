while True:
    n = int(input())
    if n == 0:
        break

    original = []
    copy = []
    for i in range(n):
        s = input()
        original.append(s)
        copy.append(s.lower())

    copy.sort()
    for i in original:
        if i.lower() == copy[0]:
            print(i)
            break
