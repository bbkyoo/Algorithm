t = int(input())

for _ in range(t):
    n = int(input())
    p_1 = 0
    p_2 = 0
    for i in range(n):
        p1, p2 = map(str, input().split())
        if p1 == 'R' and p2 == 'P':
            p_2 += 1
        elif p1 == 'P' and p2 == 'R':
            p_1 += 1
        elif p1 == 'R' and p2 == 'S':
            p_1 += 1
        elif p1 == 'S' and p2 == 'R':
            p_2 += 1
        elif p1 == 'P' and p2 == 'S':
            p_2 += 1
        elif p1 == 'S' and p2 == 'P':
            p_1 += 1
        else:
            continue
    if p_1 > p_2:
        print('Player 1')
    elif p_1 < p_2:
        print('Player 2')
    else:
        print('TIE')



