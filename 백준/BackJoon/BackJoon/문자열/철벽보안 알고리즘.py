import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = []
    for i in range(3):
        s.append(input().split())

    s_num = []
    for k in range(n):
        s_num.append(s[1].index(s[0][k]))

    for n in s_num:
        print(s[2][n], end=' ')
    print()
