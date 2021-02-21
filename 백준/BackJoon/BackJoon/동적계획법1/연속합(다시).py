# 1) 왼쪽부터 더한 값과 현재 값 중의 max값
# 2) 현재까지의 최댓값과 result 중의 max값

n=int(input())
origin=[0]
origin+=list(map(int,input().split()))

temp=[0 for _ in range(n+1)]
result=-1001

for i in range(1,n+1):
    temp[i] = max(temp[i-1] + origin[i], origin[i])
    result=max(result,temp[i])
print(result)