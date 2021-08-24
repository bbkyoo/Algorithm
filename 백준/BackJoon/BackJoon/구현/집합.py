import sys

input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    a = input().strip().split()

    if a[0] == 'add':
        s.add(int(a[1]))

    elif a[0] == 'remove':
        if int(a[1]) in s:
            s.discard(int(a[1]))

    elif a[0] == 'check':
        if int(a[1]) in s:
            print(1)
        else:
            print(0)

    elif a[0] == 'toggle':
        if int(a[1]) in s:
            s.discard(int(a[1]))
        else:
            s.add(int(a[1]))

    elif a[0] == 'all':
        s = set([i for i in range(1, 21)])

    else:
        s = set()







