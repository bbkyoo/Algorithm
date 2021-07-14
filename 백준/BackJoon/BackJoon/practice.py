from bisect import bisect_left, bisect_right
 
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)

    if right_index - left_index <= 1:
        return -1
    else:
        return right_index - left_index

n, x = map(int, input().split())
a = list(map(int, input().split()))

print(count_by_range(a,x,x))
