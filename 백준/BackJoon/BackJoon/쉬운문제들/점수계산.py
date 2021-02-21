n = list(int(input()) for __ in range(8))
n_st = sorted(n)

index = []

for i in range(8):
    if n_st[7] == n[i]:
        index.append(i+1)
    elif n_st[6] == n[i]:
        index.append(i+1)
    elif n_st[5] == n[i]:
        index.append(i+1)
    elif n_st[4] == n[i]:
        index.append(i+1)
    elif n_st[3] == n[i]:
        index.append(i+1)

index.sort()

print(sum(n_st[3:8]))
for i in range(len(index)):
    print(index[i], end=' ')