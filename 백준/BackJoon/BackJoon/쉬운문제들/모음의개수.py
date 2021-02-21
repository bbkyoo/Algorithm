moem = ['a','e','i','o','u','A','E','I','O','U']
while True:
    N = input()
    count = 0
    if N == '#':
        break
    for i in range(len(N)):
        if N[i] in moem:
            count += 1
    print(count)