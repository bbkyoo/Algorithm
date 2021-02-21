N = int(input())

result = 0
c = []
for _ in range(N):
    c.append(int(input()))

c.sort(reverse = True)    

if N < 3:
    print(sum(c))
else:
    for i in range(N):
        if (i+1) % 3 == 0:
            continue
        else:
            result += c[i]
    print(result)