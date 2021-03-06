import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
height = 0
ans = 1000000000000000000000000000000

for i in range(257):
    max = 0
    min = 0
    for j in range(n):
        for k in range(m):
            if land[j][k] < i:
                min += (i - land[j][k])
            else:
                max += (land[j][k] - i)

    inventory = max + b
    if inventory < min:
        continue

    time = 2 * max + min
    if time <= ans:
        ans = time
        height = i

print(ans, height)