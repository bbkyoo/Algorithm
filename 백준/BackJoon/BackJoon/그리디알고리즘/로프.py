N = int(input())

lope = []
for _ in range(N):
    lope.append(int(input()))

lope.sort(reverse = True)

for i in range(N):
    lope[i] = lope[i] * (i+1)

print(max(lope))
