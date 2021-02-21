N = int(input())

numbers = list(map(int, input().split()))
ormack = []
ormack.append(numbers[0])
mx = 0 
for i in range(1,N):
    if ormack[-1] < numbers[i]:
        ormack.append(numbers[i])
    else:
        mx = max(mx, ormack[-1] - ormack[0])
        ormack = [numbers[i]]

if len(ormack) > 1:
    mx = max(mx, ormack[-1] - ormack[0])

print(mx)