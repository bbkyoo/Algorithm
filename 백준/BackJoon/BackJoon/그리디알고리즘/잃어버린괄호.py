# - 를 기준으로 나누는 것이 포인트 이다.

n = input().split('-') # 이러면 -를 기준으로 리스트가 나뉘게 된다

num = []
for i in n:
    cnt = 0
    s = i.split('+')
    
    for j in s:
        cnt += int(j)
    num.append(cnt)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]

print(result)