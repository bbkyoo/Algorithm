import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
c = int(input())

d = []
for _ in range(n):
    d.append(int(input()))
d.sort()


mx = c // a

for i in range(len(d)):
    sum = c
    sum += d[i]
    k = 1
    mx = max(mx, sum//(a+(k*b)))
    for j in range(i+1,len(d)):
        sum += d[j]
        k += 1
        mx = max(mx, sum//(a+(k*b)))

print(mx)