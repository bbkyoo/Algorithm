# 연속 3잔을 마시지 않아야 하므로
# 1 : 이번 포도주를 먹고 이전 포도주를 먹지 않은 경우
# 2 : 이번 포도주를 먹고 이전 포도주도 먹은 경우
# 3 : 이번 포도주를 먹지 않아야 하는 경우
# 위 세가지 경우를 고려하여 max

n = int(input())

grape = [ int(input()) for i in range(n) ] 
dp = [0]
dp.append(grape[0])
if n > 1:
    dp.append(grape[0] + grape[1])


for i in range(3, n+1):
    case_1 = grape[i-1] + dp[i-2]
    case_2 = grape[i-1] + grape[i-2] + dp[i-3]
    case_3 = dp[i-1]
    max_value = max(case_1, case_2, case_3)

    dp.append(max_value)

print(dp[-1])