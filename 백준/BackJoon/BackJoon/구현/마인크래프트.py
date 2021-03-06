# 잘 생각해야 될것이 b개의 블록의 갯수 인데
# 이 갯수는 뺴지는 값과 , 더해지는 값을 따로 계산해서
# 다 끝나고 정산해보고 빼지는 값이 더해지는 값보다 커지면 끝인거고
# 그게 아니라면 내가 생각한 것을 실행한다.

import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
height = 0
ans = 1000000000000000000000000000000

for i in range(257):
    max = 0
    min = 0
    for j in range(n):
        for k in range(m):
            if land[j][k] < i:
                min += (i - land[j][k])
            else:
                max += (land[j][k] - i)

    inventory = max + b
    if inventory < min:
        continue

    time = 2 * max + min
    if time <= ans:
        ans = time
        height = i

print(ans, height)