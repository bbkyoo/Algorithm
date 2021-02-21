import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    num = float(input())
    arr.append(num)

result = 0
for i in range(n):
    sum = 1
    for j in range(i,n):
        sum = sum * arr[j]
        result = max(result, sum)

print("%.3f" %result)

