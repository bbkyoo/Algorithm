import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

answer = 1
cnt_mx = 1
cnt_mn = 1

for i in range(1, len(arr)):
    if arr[i] >= arr[i-1]:
        cnt_mx += 1
    else:
        answer = max(answer, cnt_mx)
        cnt_mx = 1

for i in range(1, len(arr)):
    if arr[i] <= arr[i-1]:
        cnt_mn += 1
    else:
        answer = max(answer, cnt_mn)
        cnt_mn = 1

answer = max(answer, cnt_mx, cnt_mn)
print(answer)

