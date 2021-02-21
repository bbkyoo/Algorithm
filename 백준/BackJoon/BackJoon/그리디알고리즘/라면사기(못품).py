# i번 공장에서 라면을 하나 구매한다(1 ≤ i ≤ N). 이 경우 비용은 3원이 든다.
# i번 공장과 (i+1)번 공장에서 각각 라면을 하나씩 구매한다(1 ≤ i ≤ N-1). 이 경우 비용은 5원이 든다.
# i번 공장과 (i+1)번 공장, (i+2)번 공장에서 각각 라면을 하나씩 구매한다(1 ≤ i ≤ N-2). 이 경우 비용은 7원이 든다.

n = int(input())

nudle = list(map(str, input().split('0')))

result = 0
for i in range(len(nudle)):
    if nudle[i] == '1 1':
        result += 5
    elif nudle[i] == '1 1 1':
        result += 7
    else:
        result += (3 * int(nudle[i]))

print(nudle)    
        