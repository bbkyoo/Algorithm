n = int(input())

lst = []

for i in range(n+1):
    for j in range(n+1-i):
        for k in range(n+1-i-j):
            t = n - i - j - k
            total = i * 1 + j * 5 + k * 10 + t * 50
            lst.append(total)

print(len(set(lst)))