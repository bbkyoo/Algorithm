n = int(input())
arr = list(map(int, input().split()))
dic = {}

answer = []

for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

cnt = 0
for i in arr:
    if i in dic:
        if dic[i] == 2: 
            cnt += 1
        else:
            cnt -= 1
        dic[i] -= 1        

    answer.append(cnt)

print(max(answer))