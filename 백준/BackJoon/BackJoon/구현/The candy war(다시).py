def plusOneCandy(candy):
    for i in range(len(candy)):
        if candy[i] % 2 != 0:
            candy[i] += 1

# 중요한 개념은 그냥 기존 리스트에서 빼고 기존 리스트를 갖고 행동하여라
def gameStart(candy):
    cycle = 0

    while len(set(candy)) != 1:
        temp = []
        cycle += 1

        for i in range(len(candy)):
            account = candy[i] // 2
            candy[i] -= account
            temp.append(account)

        for j in range(-1, len(candy) -1):
            candy[j+1] += temp[j]

        plusOneCandy(candy)

    return cycle

t = int(input())

for _ in range(t):
    n = int(input())
    candy = list(map(int, input().split()))
    plusOneCandy(candy)
    print(gameStart(candy))



















