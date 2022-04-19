n = int(input())
arr = []
sm = 0
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)
    sm += line[1]

if sm % 2 == 0:
    mid = sm // 2
else:
    mid = sm // 2 + 1

arr.sort()
result = 0
cnt = 0
for i in range(n):
    cnt += arr[i][1]
    if mid <= cnt:
        result = arr[i][0]
        break

print(result)