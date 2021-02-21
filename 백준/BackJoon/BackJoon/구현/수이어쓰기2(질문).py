import sys

input = sys.stdin.readline

n, k = map(int, input().split())

s = ''

for i in range(1,n+1):
    s += str(i)

try:
    print(s[k-1])
except:
    print(-1)