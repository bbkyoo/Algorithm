x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = 0, 0

if x2 == x3 and (x1 >= x2 or x1 <= x2):
    x4 = x1
elif x1 == x3 and (x2 >= x1 or x2 <= x1) :
    x4 = x2
elif x2 == x1 and (x3 >= x1 or x3 <= x1) :
    x4 = x3

if y2 == y3 and (y1 >= y2 or y1 <= y2):
    y4 = y1
elif y1 == y3 and (y2 >= y1 or y2 <= y1) :
    y4 = y2
elif y2 == y1 and (y3 >= y1 or y3 <= y1) :
    y4 = y3

print(x4, y4)

