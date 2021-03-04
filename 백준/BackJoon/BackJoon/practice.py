import sys

input = sys.stdin.readline

length, width, height = map(int, input().split())
box = length * width * height
n = int(input())
max_count = 0
cube = []

for i in range(n):
    a, b = map(int, input().split())
    cube.append([(2**a)*(2**a)*(2**a) , b])
    max_count += b

count = 0
while box >= 0 and max_count and n:
    n -= 1
    while cube[n][1] and box >= cube[n][0]:
        box -= cube[n][0]
        cube[n][1] -= 1
        max_count -= 1
        count += 1
           
if box != 0:
    print(-1)
else:
    print(count)
