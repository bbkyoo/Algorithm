n, c = map(int, input().split())
arr = list(map(int, input().split()))

dic = {}

for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

lst = []

for i in dic.keys():
    lst.append([i, dic[i]])

lst.sort(key=lambda x : -x[1])

answer = []

for i in lst:
    for j in range(i[1]):
        answer.append(i[0])

print(*answer)