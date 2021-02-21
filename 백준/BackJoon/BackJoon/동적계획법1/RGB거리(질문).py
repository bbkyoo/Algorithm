# https://chunghyup.tistory.com/48
# 0, 1, 2는 각각 빨강, 초록, 파랑을 뜻하고
# p[i][0]은 i번째집을 빨강으로 칠했을때의 최솟값을 나타낸다.
# p[i][1]과 p[i][2]도 마찬가지로 i번째집을 초록, 파랑으로 칠했을때의 최솟값을 나타낸다.
# 이 3개의 값중에서 가장 작은 값을 출력해주면 된다.

n = int(input())

lt = []
for _ in range(n):
    lt.append(list(map(int, input().split()))) # 빨 초 파 비용

for i in range(1, len(lt)):
    lt[i][0] = min(lt[i-1][1], lt[i-1][2] + lt[i][0])
    lt[i][1] = min(lt[i-1][0], lt[i-1][2] + lt[i][1])
    lt[i][2] = min(lt[i-1][0], lt[i-1][1] + lt[i][2])

print(min(lt[n-1][0], lt[n-1][1], lt[n-1][2]))