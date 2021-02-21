# 1) 0을 포함한 음수는 작은 수 부터 묶는다.
# 3) 1보다 큰 수는 큰 수부터 묶는다.
# 2) 숫자가 1인 경우에는 묶지 않는다.

N = int(input())

nums = [int(input()) for i in range(N)]
dp = []

negative = []
positive = []
ans = 0

for num in nums:
    if num <= 0:    # 0도 negative의 원소로 둔다
        negative.append(num)
    elif num == 1:
        ans += 1    # 숫자가 1인 경우에는 묶지 않으므로 미리 계산하여 둔다.
    elif num >= 0:
        positive.append(num)

negative.sort()
positive.sort(reverse = True)


# 여기 두 개씩 곱하는 알고리즘을 잘 기억!!
        
# 작은 수 부터 차례대로 묶는다
for i in range(0, len(negative), 2):
    if i+1 < len(negative):
        ans += negative[i] * negative[i+1]
    else:
        ans += negative[i]

# 큰 수 부터 차례대로 묶는다
for i in range(0, len(positive), 2):
    if i+1 < len(positive):
        ans += positive[i] * positive[i+1]
    else:
        ans += positive[i]

print(ans)        