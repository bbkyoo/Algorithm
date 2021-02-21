N = int(input())

money = 1000 - N
count = 0

while money:
    if money >= 500:
        money -= 500
        count += 1
    elif money >= 100 and money < 500:
        money -= 100
        count += 1
    elif money >= 50 and money < 100:
        money -= 50
        count += 1
    elif money >= 10 and money < 50:
        money -= 10
        count += 1
    elif money >= 5 and money < 10:
        money -= 5
        count += 1
    else:
        money -= 1
        count += 1

print(count)