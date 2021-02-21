N = int(input())
A = list(map(int, input().split()))
dp = [0]

for i in range(N):
    low = 0
    high = len(dp) - 1

    while low <= high: # A[i]보다 작거나 같은 수 중에서 제일 큰거 위치 찾기
        mid = (low + high) //2
        if dp[mid] < A[i]:
            low = mid + 1
        else:
            high = mid - 1

    if low >= len(dp): # 위치가 배열보다 크다면 넣어준다
        dp.append(A[i])
    else:              # 해당위치의 숫자를 바꿔준다. 항상 작거나 같은수를 반환하기때문에 비교하지 않아도 된다.
        dp[low] = A[i]

print(len(dp) - 1)