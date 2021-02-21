import sys

# 이 코드는 아예 외워버리기

n = int(sys.stdin.readline())

s = []
op = []
count = 1
temp = True
for i in range(n):
    num = int(sys.stdin.readline())
    while count <= num: # 이 while문이 가장 중요
        s.append(count)
        op.append('+')
        count += 1

    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        temp = False

if temp == False:
    print('NO')
else:
    for i in op:
        print(i)