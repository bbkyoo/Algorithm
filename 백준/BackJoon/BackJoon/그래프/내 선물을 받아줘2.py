#  E가 쓰여져 있는 칸에 서 있었다면, (1, x+1)로, W의 경우에는 (1, x-1)로 순간이동

n = int(input())

arr = list(input())
ans = 0

for i in range(n-1):
    if arr[i] == 'E' and arr[i+1] == 'W':
        ans += 1

print(ans)