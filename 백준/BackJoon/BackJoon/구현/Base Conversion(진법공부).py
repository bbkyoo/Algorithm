a, b = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))

ten = 0
answer =[]

# 이런 어떤 진법을 10진법으로 변환하는 것을 잘 알아두기
# 그냥 맨 아래부터 제곱으로 더하기

for i in range(m):
    ten += nums[-1]*(a**i)
    nums.pop(-1)

while ten != 0:
    answer.append(str(ten % b))
    ten = ten // b

answer.reverse()

print(" ".join(answer))

