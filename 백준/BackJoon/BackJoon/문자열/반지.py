c = input()
n = int(input())
count = 0

for _ in range(n):
    s = input()

    if c in s:
        count += 1

    else:
        for i in range(1, len(c)):
            if s[-(len(c)-i):] + s[:i] == c:
                count += 1

print(count)