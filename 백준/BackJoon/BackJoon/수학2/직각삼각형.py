import math

while True:
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break
    if x == math.sqrt(y**2 + z**2):
        print("right")
    elif y == math.sqrt(x**2 + z**2):
        print("right")
    elif z == math.sqrt(x**2 + y**2):
        print("right")
    else:
        print("wrong")