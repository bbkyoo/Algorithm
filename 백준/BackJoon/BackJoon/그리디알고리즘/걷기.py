x, y, w, s = map(int, input().split())

case1 = (x + y) * w
case2 = (min(x,y) * s) + abs(x-y) * w 
case3 = max(x, y) * s if (x + y) % 2 == 0 else (max(x, y) - 1) * s + w

print(min(case1, min(case2, case3)))