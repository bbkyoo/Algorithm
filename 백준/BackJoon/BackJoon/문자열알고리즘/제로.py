k = int(input())

lt = []
for _ in range(k):
    temp = int(input())
    if temp == 0:
        lt.pop()
    else:
        lt.append(temp)

print(sum(lt))
    