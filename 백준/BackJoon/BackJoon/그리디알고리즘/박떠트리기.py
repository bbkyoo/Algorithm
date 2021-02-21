# N개의 공을 K개의 바구니에 빠짐없이 나누어 담는다.
# 각 바구니에는 1개 이상의 공이 들어 있어야 한다.
# 각 바구니에 담긴 공의 개수는 모두 달라야 한다.
# 가장 많이 담긴 바구니와 가장 적게 담긴 바구니의 공의 개수 차이가 최소가 되어야 한다.

# 나눠 담을 수 있는지 여부를 결정하고 
# 담을 수 있는 경우에는 가장 많이 담긴 바구니와 가장 적게 담긴 바구니의 공의 개수 차이를 계산

n, k = map(int, input().split())

limit = 0
for i in range(1, k+1):
    limit += i

if n < limit:
    print(-1)
else:


# 8 3
# 1 3 4