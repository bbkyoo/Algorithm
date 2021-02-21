su = int(input())

ht = []

for i in range(su):
    H, W, N = map(int,input().split())
    num = 101
    for j in range(W):
        for k in range(H):
            ht.append(num)
            num += 100
        num += 1
        num -= H * 100
    print(ht[N-1])
    del ht[:]











