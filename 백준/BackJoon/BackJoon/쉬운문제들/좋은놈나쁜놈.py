n = int(input())

for _ in range(n):

    g_count = 0
    b_count = 0
    sentence = input()
    for i in sentence:
        if i == 'g' or i == 'G':
            g_count += 1
        elif i == 'b' or i == 'B':
            b_count += 1

    if g_count == b_count:
        sentence += ' is NEUTRAL'
    elif g_count > b_count:
        sentence += ' is GOOD'
    else:
        sentence += ' is A BADDY'

    print(sentence)