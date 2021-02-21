import sys
sys.setrecursionlimit(10**9)

n = int(input())

arr = [['*'] * n for _ in range(n)]

temp = n
cnt = temp//3

for ct in range(cnt):
    idx = []
    for i in range(n):
        if (i // 3**ct) % 3 == 1:
            idx.append(i)
 
    for i in idx:
        for j in idx:
            arr[i][j] = " "

for i in arr:
    for j in i:
        print(j, end="")
    print()
