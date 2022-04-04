r, c = map(int, input().split())

matrix = []
for _ in range(r):
    matrix.append(list(map(int, input().split())))

result = ''
if r % 2 != 0:
    for i in range(r):
        if i % 2 == 0:
            result += 'R' * (c-1)
        else:
            result += 'L' * (c-1)
        if i != r-1:
            result += 'D'
elif c % 2 != 0:
    for i in range(c):
        if i % 2 == 0:
            result += 'D' * (r-1)
        else:
            result += 'U' * (r-1)
        if i != c-1:
            result += 'R'