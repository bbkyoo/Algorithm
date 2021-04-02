import sys

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    temp = input().split()
    if temp[1] == 'enter':
        arr.append(temp[0])

    elif temp[1] == 'leave':
        arr.pop(arr.index(temp[0]))

arr.sort(reverse=True)
for i in arr:
    print(i)