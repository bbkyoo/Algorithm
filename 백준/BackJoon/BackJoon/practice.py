import sys

input = sys.stdin.readline

n, b = input().split()
dic = {}
num = 10

for i in range(65, 91):
    dic[chr(i)] = num
    num += 1

n = list(n)
n.reverse()

result = 0
for i in range(len(n)):
    if n[i] in dic:
        result += (dic[n[i]]) * (int(b)**i)
    else:
        result += (int(n[i])) * (int(b)**i)

print(result)