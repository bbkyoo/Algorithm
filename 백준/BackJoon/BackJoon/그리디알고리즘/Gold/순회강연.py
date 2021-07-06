# 최대로 돈을 벌기 위해서 데드라인인 d안에서 가장 많은 돈을 주는 강연을 가면 된다.
# 따라서 입력값을 데드라인을 기준으로 오름차순으로 정렬한다.
# 이후 반복문을 순회하면서 heapq 리스트에 값을 추가하고
# 리스트의 길이와 데드라인을 비교한다.
# 리스트의 길이가 데드라인보다 클 경우 데드라인을 넘긴 강연이 있는 것이기 때문에
# pop을 이용하여 리스트 값 중 가장 작은 값을 제거한다.
# 반복문이 끝나고 리스트의 값을 모두 더하여 출력한다.

import sys
import heapq

input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    p, d = map(int, input().split())
    nums.append([d, p])

nums.sort(key = lambda x : x[0])
sums = []

for num in nums:  # 이 부분이 가장 중요 꼭 이 알고리즘을 외우고 써먹기     
    heapq.heappush(sums, num[1])
    if len(sums) > num[0]:
        heapq.heappop(sums)

print(sum(sums))












