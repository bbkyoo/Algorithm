# 주어진 숫자들로 조합할 수 없는 최솟값을 구하여라

N = int(input())

chu = list(map(int, input().split()))
chu.sort()

num = 1
for i in range(N): # 이렇게 하면 주어진 숫자들로 조합할 수 없는 최솟값을 구할 수 있다.
    if num < chu[i]:
        break
    num += chu[i]

print(num)

