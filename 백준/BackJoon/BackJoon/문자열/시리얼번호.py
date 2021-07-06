n = int(input())

s = []
for _ in range(n):
    count = 0
    command = input()
    for c in command:
        if c.isdigit():
            count += int(c)

    s.append((command, count))

s.sort(key = lambda x: (len(x[0]),x[1],x[0]))

for i in s:
    print(i[0])

