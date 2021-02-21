num = int(input())
count = 1

while num > count:
    num -= count
    count += 1

if count % 2 != 0:
    up = count - num + 1
    down = num
else:
    down = count - num + 1
    up = num

print(str(up) + '/' + str(down))