n = int(input())
cow = {}

count = 0
for _ in range(n):
    num, state = map(int, input().split())
    if num not in cow:
        cow[num] = state
    else:
        if cow[num] != state:
            cow[num] = state
            count += 1

print(count)