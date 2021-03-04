import sys

input = sys.stdin.readline

dic = {}
for i in range(10):
    dic[str(i)] = 0
n = input().rstrip()
cnt = 0

for i in range(len(n)):
    if n[i] in ["6", "9"]:
        dic["6"] += 1
    else:
        dic[n[i]] += 1

if dic["6"] % 2 == 0:
    dic["6"] = dic["6"] // 2
else:
    dic["6"] = dic["6"] // 2 + 1

print(max(dic.values()))

