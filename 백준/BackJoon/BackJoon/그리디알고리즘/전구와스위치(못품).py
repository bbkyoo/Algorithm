def change_OnOFF(value):
    if value == "0":
        value = "1"
    else:
        value = "0"
    return value

def change(n, t):
    if n == 0:
        t[0] = change_OnOFF(t[0])
        t[1] = change_OnOFF(t[1])
    elif n == N-1:
        t[-1] = change_OnOFF(t[-1])
        t[-2] = change_OnOFF(t[-2])
    else:
        t[n-1] = change_OnOFF(t[n-1])
        t[n] = change_OnOFF(t[n])
        t[n+1] = change_OnOFF(t[n+1])
    return t

N = int(input())
count = 0
current = list(input().strip())
result = list(input().strip())
temp = current[:]
count_list = []
isEnd = False

if current == result:
    print(0)
else:
    # 첫번째 스위치를 안누른 경우
    for i in range(1,N):
        # 바로 전 값이 다를 경우
        if temp == result:
            print(count)
            isEnd = True
            break
        elif i == N-1:
            temp = change(i, temp)
            if temp == result:




























































