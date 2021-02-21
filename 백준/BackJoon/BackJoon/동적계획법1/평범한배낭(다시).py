# dp [i][j] = max(dp[i - 1][j], dp[i - 1][j - weight [i]] + value [i]]
# dp [i - 1][j]: i번째 아이템을 챙기지 않았을 때의 최댓값
# dp [i - 1][j - weight [i]] + value [i]: i번째 아이템을 챙겼을 때 갖는 최댓값
# https://dojinkimm.github.io/algorithm/2019/10/19/dp-2.html

N, K = map(int ,input().split())

item = [[0,0]]

for _ in range(N):
    W, V = map(int, input().split())
    item.append([W,V])

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= item[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-item[i][0]] + item[i][1])
        else:
            dp[i][j] = dp[i-1][j]
        
print(dp[N][K])
 
































