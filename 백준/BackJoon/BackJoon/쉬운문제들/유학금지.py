x = 'CAMBRIDGE'
N = list(input())

for i in x:
    for j in range(len(N)):
        if N[j] == i:
            N[j] = ''

for i in N:
    print(i, end="")