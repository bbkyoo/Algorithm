lt = []

for i in range(1,31):
    lt.append(i)

lt.sort()

for _ in range(28):
    n = int(input())
    lt.pop(lt.index(n))

for i in lt:
    print(i)