# https://sooooooyn.tistory.com/12

def sol(idx):
    global result

    if idx == len(s):
        result = 1
        return
    if dp[idx]:
        return
    dp[idx] = 1

    for i in range(len(a)):
        if len(s[idx:]) >= len(a[i]):
            for j in range(len(a[i])):
                if a[i][j] != s[idx+j]:
                    break
            else:
                sol(idx+len(a[i]))
    return

s = input()
n = int(input())
dp = [0] * 101

a = []
for _ in range(n):
    a.append(input())

result = 0
sol(0)
print(result)
