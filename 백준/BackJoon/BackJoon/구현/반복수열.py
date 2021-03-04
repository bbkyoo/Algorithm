import sys

input = sys.stdin.readline

a, p = map(int, input().split())

lt = [a]

while True:
    current = lt[-1]
    current = list(str(current))
    sum = 0
    for i in range(len(current)):
        sum += int(current[i])**p
    
    if sum in lt:
        break
    else:
        lt.append(sum)

cnt = 0
for i in lt:
    if sum == i:
        break
    else:
        cnt += 1

print(cnt)