# 부피로 계산 했을때 치명적인 반례
# 가령, 박스의 길이가 3 X 4 X 8일 경우 부피는 96이고, 이 곳에 4 X 4 X 4 큐브를 넣는다고 가정해 봅시다.
# 부피만 계산하면, 4 X 4 X 4 큐브는 64라서 가능할 것처럼 보이지만, 실제로 생각을 해보면 큐브가 박스에 넣는 것은 불가능한 것을 알 수 있습니다.
# 그렇다면, 이 문제를 어떻게 해결할 수 있을까요?
# 바로, 박스 자체를 2^n x 2^n x 2^n으로 분할해 보면서 가지고 있는 큐브를 집어 넣어보는 것입니다.

import sys

input = sys.stdin.readline

length, width, height = map(int, input().split())
N = int(input())

box = length * width * height

cube = []

for _ in range(N):
    a, b = map(int, input().split())
    cube.append([(2**a)*(2**a)*(2**a) ,b])

mx_c = 0
for i in range(len(cube)):
    mx_c += cube[i][1]

count = 0

while box > 0 and mx_c and N:
    N -= 1
    while box >= cube[N][0] and cube[N][1]:
        box -= cube[N][0]
        cube[N][1] -= 1
        mx_c -= 1
        count += 1

if box != 0:
    print(-1)
else:
    print(count)







