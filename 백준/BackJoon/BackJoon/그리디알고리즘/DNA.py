import sys

input = sys.stdin.readline
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(input())

arr.sort()
answer = ''
for i in range(m):
    temp = {}
    for j in range(n):
        if arr[j][i] not in temp:
            temp[arr[j][i]] = 1
        else:
            temp[arr[j][i]] += 1
    temp2 = []
    for i, v in temp.items():
        temp2.append([i, v])
    temp2.sort(key=lambda x:(-x[1],x[0]))
    answer += temp2[0][0]

val = 0
for i in range(n):
    for j in range(m):
        if answer[j] != arr[i][j]:
            val += 1

print(answer)
print(val)