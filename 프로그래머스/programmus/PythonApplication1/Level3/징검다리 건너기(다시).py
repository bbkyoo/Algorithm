# https://covenant.tistory.com/162

import copy

inf = 200000000

def solution(stones, k):
    left = 1 
    right = inf

    while left <= right:
        mid = (left + right) // 2
        temp = copy.deepcopy(stones)

        for i in range(len(temp)):
            temp[i] -= mid

        cnt = 0
        check = False
        
        for i in range(len(temp)):
            if temp[i] <= 0:
                cnt += 1
            else:
                cnt = 0

            if cnt >= k:
                check = True
                break

        if check:
            right = mid - 1
        else:
            left = mid + 1

    return left