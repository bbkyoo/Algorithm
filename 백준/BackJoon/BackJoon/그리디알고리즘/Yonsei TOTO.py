n, m = map(int, input().split())
result = 0
arr = []
for _ in range(n):
    p = list(map(int, input().split()))
    l = list(map(int, input().split()))
    if p[0] < p[1]:
        if m:
            m -= 1
            result += 1
        else:
            print(result)
            exit()
    else:
        l.sort(reverse=True)
        arr.append(l[p[1]-1])

arr.sort()

for i in arr:
    if i <= m:
        m -= i
        result += 1
    else:
        break

print(result)