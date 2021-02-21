N = int(input())

li = []
for _ in range(N):
    num = int(input())
    li.append(num)

num = len(li) # 이거 쓸때 조심

if (li[2] - li[1]) == (li[1] - li[0]):
    result =  li[num-1] + (li[1] - li[0])

elif (li[2] // li[1]) == (li[1] // li[0]):
    result = li[num-1] * (li[1] // li[0])

print(result)