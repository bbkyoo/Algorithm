import sys

n = int(sys.stdin.readline())

for _ in range(n):
    k = list(input())
    sum = 0
    for i in range(len(k)):
        if k[i] == '(':
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            break
    if sum == 0:
        print("YES")
    else:
        print("NO")

