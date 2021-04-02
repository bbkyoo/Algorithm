a, b = input().split()

a = list(a)
b = list(b)

len_a = len(a)

result = 50
while len(a) <= len(b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1

    result = min(cnt, result)
    b.pop(0)

print(result)