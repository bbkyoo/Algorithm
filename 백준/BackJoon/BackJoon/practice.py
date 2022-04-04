n, k = map(int, input().split())
arr = list(map(int, input().split()))
if n >= k:
    print(0)
    exit()

a = []
for i in range(n):
    a.append(arr.pop(0))

for i in arr:
    if i not in a:
        a.pop()
        a.append(i)

