# 딸 -> 초 -> 바 -> 딸
# 0 -> 딸기우유
# 1 -> 초코우유
# 2 -> 바나나우유 

N = int(input())

milk = list(map(int, input().split()))

count = 0
current_milk = -1

for i in range(len(milk)):
    if milk[i] == (current_milk + 1) % 3:
        count += 1
        current_milk += 1

print(count)

