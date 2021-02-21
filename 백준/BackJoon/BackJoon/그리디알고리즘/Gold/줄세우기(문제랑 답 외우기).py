#dp[n] = n번호일때까지 연속된 증가수열의 개수
#=> dp[n] = dp[n - 1] + 1
#LCS 꼭 풀어보기

n = int(input())
line = list(map(int, input().split()))
dp = [0] * (n+1)

mx = 0

for i in range(1,n+1):
    k = line[i-1]
    dp[k] = dp[k-1] + 1
    mx = max(mx, dp[k-1] + 1)
    
print(n-mx)


