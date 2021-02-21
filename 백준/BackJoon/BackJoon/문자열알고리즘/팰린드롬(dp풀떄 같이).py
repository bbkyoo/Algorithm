# 팰린드롬인 경우에는 1, 아닌 경우에는 0
#import sys

#input = sys.stdin.readline

#N = int(input())
#board = [0] + list(map(int, input().split()))

#M = int(input())
#for _ in range(M):
#    palin = []
#    S, E = map(int, input().split())
#    for i in range(S, E+1):
#        palin.append(board[i])

#    palin_rev = list(reversed(palin))
    
#    if palin_rev == palin:
#        print(1)
#    else:
#        print(0)

N = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):#길이가 1일때
    dp[i][i]=1
    if i < N-1 and num_list[i] == num_list[i+1]:#길이가 2일때
        dp[i][i+1]=1
 
for i in range(1,N):
    for j in range(1,i+1):
        if num_list[i]==num_list[i-j] and dp[i-j+1][i-1]==1:
            dp[i-j][i]=1
 
M=int(sys.stdin.readline())
for _ in range(M):
    S,E=map(int,sys.stdin.readline().split())
    print(dp[S-1][E-1])
