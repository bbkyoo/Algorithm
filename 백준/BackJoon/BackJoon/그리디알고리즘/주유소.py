# 원 안에 있는 숫자는 그 도시에 있는 주유소의 리터당 가격이다. 
# 도로 위에 있는 숫자는 도로의 길이를 표시한 것이다. 

N = int(input())

length = list(map(int, input().split()))
price = list(map(int, input().split()))

k = 0
start = price[0]
result = price[0] * length[0]

for i in range(1, N):
    if start > price[i]:
        start = price[i]
        result += start * length[k+1]
    else:
        result += start * length[k+1]
    k += 1
    
    if k == N-2:
        break

print(result)