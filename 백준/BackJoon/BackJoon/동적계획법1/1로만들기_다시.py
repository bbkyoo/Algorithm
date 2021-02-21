# 입력한 숫자로 세가지 연산을 모두 수행하여(1,2번 연산은 가능할 때만) 그 결과 값을 리스트로 저장하고, 
# 그 리스트안에 있는 각각의 숫자들을 다시 세가지 연산 모두를 수행하도록 하고, 
# 각 루프 한번당 count를 1씩 증가시키면 어떨까요?

N = int(input())
count = 0
minimum = [N]

def cal(N):
    list = []
    for i in N:
        list.append(i-1)
        if i%3 == 0:
            list.append(i/3)
        if i%2 == 0:
            list.append(i/2)
    return list

while True:
    if N == 1:
        break
    
    temp = minimum
    minimum = cal(temp)
    count += 1

    if min(minimum) == 1:
        break
    
print(count)