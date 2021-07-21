import sys

input = sys.stdin.readline

owned = set()

n, q = map(int, input().split())

for _ in range(q):
    x = int(input())
    node, isOwned, num = x, False, 0
    while node > 0:
        if node in owned:
            isOwned = True
            num = node
        node //= 2
    print(num)
    if not isOwned:
        owned.add(x)