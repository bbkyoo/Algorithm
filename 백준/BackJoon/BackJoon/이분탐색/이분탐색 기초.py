# 이분탐색 라이브러리
from bisect import bisect_left, bisect_right

# 지정한 왼쪽 값과 오른쪽 값 사이에 원소의 갯수 구하기 
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a, -1, 3))
