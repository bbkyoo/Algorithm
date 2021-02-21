t = int(input())

for _ in range(t):
    n = int(input())
    card = list(map(str, input().split()))

    q = [card[0]]

    for i in range(1,len(card)):
        if q[0] >= card[i]:
            q.insert(0,card[i])
        else:
            q.append(card[i])

    for i in q:
        print(i, end='')
    print()

    
    