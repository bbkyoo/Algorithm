# https://jjangsungwon.tistory.com/123

from collections import defaultdict

n = int(input())
arr = []
for i in range(n):
    c, s = map(int, input().split())
    arr.append([i+1, c, s])

arr.sort(key=lambda x:(x[2]))
answer = defaultdict(int)
dic = defaultdict(int)
total = 0

j = 0
for i in range(n):
    while arr[j][2] < arr[i][2]:
        total += arr[j][2]
        dic[arr[j][1]] += arr[j][2]
        j += 1
    answer[arr[i][0]] = total - dic[arr[i][1]] # 총합 - 현재 누적된 같은 색깔이 공의 크기

for i in range(1, n+1):
    print(answer[i])
