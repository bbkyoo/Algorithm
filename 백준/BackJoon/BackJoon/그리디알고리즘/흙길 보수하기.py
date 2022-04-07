n, l = map(int, input().split())

arr = []
idx = 0
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort()

start = arr[0][0]
total_count = 0

for a, b in arr:
    if start > b:
        continue
    elif start < a:
        start = a
    dist = b - start
    remainder = 1
    if dist % l == 0:
        remainder = 0
    count = dist // l + remainder
    start += count * l
    total_count += count

print(total_count)