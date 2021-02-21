t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    temp1 = 1
    temp2 = 1

    if m-n == 0:
        print(1)
    else:
        for i in range(1, n+1):
            temp1 *= i

        for i in range(m-n+1, m+1):
            temp2 *= i

        print(temp2 // temp1)