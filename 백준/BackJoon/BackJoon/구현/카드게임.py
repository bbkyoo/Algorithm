card = []
for _ in range(5):
    color, number = input().split()
    card.append(color + number)

card.sort(key=lambda x : x[1])

result = 0
if card[0][0] == card[1][0] == card[2][0] == card[3][0] == card[4][0]:
    isTrue = True
    for i in range(1,5):
        if (int(card[i-1][1]) - 1 == int(card[i][1])) or (int(card[i-1][1]) + 1 == int(card[i][1])):
            continue
        else:
            isTrue = False
            break

    if isTrue:
        result = max(result, int(card[-1][1]) + 900)
    else:
        result = max(result, int(card[-1][1]) + 600)

if (card[0][1] == card[1][1] == card[2][1] == card[3][1]) or (card[1][1] == card[2][1] == card[3][1] == card[4][1]):
    result = max(result, int(card[1][1]) + 800)

if (card[0][1] == card[1][1] == card[2][1] and card[3][1] == card[4][1]):
    result = max(result, 10*int(card[0][1]) + int(card[3][1]) + 700)

if (card[0][1] == card[1][1] and card[2][1] == card[3][1] == card[4][1]):
    result = max(result, 10*int(card[2][1]) + int(card[0][1]) + 700)

isTrue = True
for i in range(1,5):
    if int(card[i-1][1]) - 1 == int(card[i][1]) or int(card[i-1][1]) + 1 == int(card[i][1]):
        continue
    else:
        isTrue = False
        break

if isTrue:
    result = max(result, int(card[-1][1]) + 500)

if card[0][1] == card[1][1] == card[2][1]:
    result = max(result, int(card[0][1]) + 400)

if card[1][1] == card[2][1] == card[3][1]:
    result = max(result, int(card[1][1]) + 400)

if card[2][1] == card[3][1] == card[4][1]:
    result = max(result, int(card[2][1]) + 400)

if (card[0][1] == card[1][1] and card[2][1] == card[3][1]):
    result = max(result, int(card[2][1])*10 + int(card[1][1]) + 300)

if (card[1][1] == card[2][1] and card[3][1] == card[4][1]):
    result = max(result, int(card[3][1])*10 + int(card[1][1]) + 300)

if (card[0][1] == card[1][1] and card[3][1] == card[4][1]):
    result = max(result, int(card[3][1])*10 + int(card[1][1]) + 300)

if card[0][1] == card[1][1] or card[1][1] == card[2][1]:
    result = max(result, int(card[1][1]) + 200)

if card[2][1] == card[3][1] or card[3][1] == card[4][1]:
    result = max(result, int(card[3][1]) + 200)

result = max(result, int(card[-1][1]) + 100)

print(result)






















