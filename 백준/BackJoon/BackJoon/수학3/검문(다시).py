# N[0] = K[0] * M + R
# N[1] = K[1] * M + R
# N[2] = K[2] * M + R
# 나머지 R을 없애기 위해서는
# N[i]에서 N[i - 1]을 빼주면 되는데 N[1]에서 N[0]을 빼주면
# N[1] - N[0] = M * (K[1] - K[0])
# 위처럼 될 수 있다.
# K[1] - K[0]은 N[1] - N[0]의 약수임을 알 수 있다.

import math

N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()

# -------------------------------------------
# find divisor, 최대공약수 구하는 방법 외우기
mog = nums[-1] - nums[0] # 이 부분과
divisor = [mog] # 이 부분이 중요

for i in range(2, int(math.sqrt(mog)) + 1):
    if mog % i == 0:
        divisor.append(i)
        divisor.append(mog//i)

divisor = list(set(divisor))
# -------------------------------------------

divisor.sort()

# get anser, 최대공약수로 nums[i]를 나누어보아서 나머지가 다른것이 있으면 제끼고, 아니면 출력
for d in divisor:
    for i in range(N):
        if i == N - 1:
            print(d, end=" ")
        elif nums[i] % d != nums[i+1] % d:
            break