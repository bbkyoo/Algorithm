# 여기서 내가 생각한 left, right 개념을 잘 이해하고 다른 문제도 풀자

def solution(people, limit):
    people.sort()

    right = 0
    left = len(people) - 1

    count = 0
    while left >= right:
        if people[right] + people[left] > limit:
            left -= 1
            count += 1
        else:
            right += 1
            left -= 1
            count += 1
       
    return count





