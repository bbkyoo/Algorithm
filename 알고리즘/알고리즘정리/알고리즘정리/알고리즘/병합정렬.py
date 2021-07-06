import random

# 1. 병합정렬
# 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
# 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
# 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.

# 2. 구현 

def merge(left, right):
    merged = []
    left_point, right_point = 0, 0

    # case1: left와 right가 아직 남아있을 때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2: left만 남아 있을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    # case3: right만 남아 있을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged

def mergesplit(data):
    if len(data) <= 1:
        return data

    medium = int(len(data)/2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)

data = random.sample(range(100), 10)
data = mergesplit(data)
print(data)

# 3. 시간 복잡도
# O(nlog(n))





