import sys

input = sys.stdin.readline
inf = sys.maxsize

n = int(input())

result = 0
dp = [[1]*n for _ in range(n)]
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for k in range(n): # k 거쳐가는 점
    for i in range(n): # i 시작점
        for j in range(n): # j 끝점
            if i == j or j == k or k == i:
                continue

            if arr[i][j] == arr[i][k] + arr[k][j]:
                dp[i][j] = 0

            elif arr[i][j] > arr[i][k] + arr[k][j]:
                result = -1

if result != -1:
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                result += arr[i][j]

print(result)



