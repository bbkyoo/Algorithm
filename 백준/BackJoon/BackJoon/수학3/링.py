N = int(input())

temp = list(map(int, input().split()))

for i in range(1, N):
    a = temp[0]
    b = temp[i]
    while b != 0:
        a = a % b
        a, b = b, a    
    print("{}/{}".format(temp[0]//a, temp[i] // a))    
