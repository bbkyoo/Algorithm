#from itertools import combinations

#def solution(distance, rocks, n):
#    temp = list(set(combinations(rocks, n)))
#    answer = 0
#    for i in temp:
#        r = rocks.copy()
#        for j in range(len(i)-1, -1, -1):
#            if i[j] in r:
#                r.remove(i[j])

#        r.sort()
#        start = 0
#        mn = distance
#        for k in r:
#            mn = min(mn, k - start)
#            start = k
#        mn = min(mn, distance - start)     
#        answer = max(answer, mn)

#    return answer
import sys

def solution(distance, rocks, n):
    answer = 0

    rocks.sort()
    rocks.append(distance) # 마지막 도착지와 거리를 계산하기 위해 마지막 거리를 append

    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2 # mid는 거리의 최솟값 거리가 mid 이하이면 없앤다.
        min_distance = sys.maxsize

        current = 0 # 현재 위치
        remove_cnt = 0 # 바위를 제거한 개수

        for rock in rocks:
            diff = rock - current # 바위와 현재 위치 사이의 거리

            if diff < mid: # mid보다 거리가 짧으면 바위 제거
                remove_cnt += 1
            else:
                current = rock # 현재 위치를 그 바위로 옮기고
                min_distance = min(min_distance, diff) # 해당 mid단계에서의 최소거리인지 체크
                
        if remove_cnt > n: #바위를 너무 많이 제거해서 mid를 줄여 바위를 조금만 제거
            right = mid - 1
        else: # 바위를 너무 적게 제거했거나 딱 맞아서 mid를 늘려 바위를 더 제거하거나 mid 최댓값을 올려보자 
            answer = min_distance
            left = mid + 1

    return answer