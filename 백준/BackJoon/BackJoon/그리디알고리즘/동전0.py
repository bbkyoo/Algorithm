N, K = map(int, input().split())

coin = []

for i in range(N):
     coin.append(int(input()))

coin.reverse()

result = 0
for i in range(N):
    if K == 0:
        break
    result += K // coin[i]
    K %= coin[i]
    
print(result)
    

    
