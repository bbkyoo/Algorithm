N = int(input())

result = 1
for i in range(1,N+1):
    result *= i

lt = []
while result != 0:
    lt.append(result % 10)
    result = result // 10

count = 0
for i in range(len(lt)):
    if lt[i] == 0:
        count += 1
    else:
        break

print(count)