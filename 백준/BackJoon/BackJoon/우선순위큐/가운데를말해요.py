import heapq
import sys

input = sys.stdin.readline

# 중앙값 기준으로 작은 값 = left, 큰 값 = right
left, right = [], []

N = int(input())

for _ in range(N):
    num = int(input())
    # left(max_heap)의 루트 노드가 중간값
    # max_heap의 루트는 항상 min_heap의 루트보다 같거나 작아야 한다.
    if len(left) == len(right): # max_heap과 min_heap의 노드수가 같다면 
        # max_heap
        heapq.heappush(left, (-num, num))
    else: # max_heap과 min_heap의 노드수가 다르다면
        # min_heap
        heapq.heappush(right, (num, num))

    # 오른쪽 값에 원소가 있으면서,
    # 왼쪽 값이 오른쪽 값보다 큰 경우... left 원소보다 right원소가 더 커야 하는 조건에 위배
    if right and left[0][1] > right[0][1]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(right, (left_value,left_value))
        heapq.heappush(left, (-right_value,right_value))
    print(left[0][1])

