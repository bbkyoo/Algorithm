from itertools import permutations

def solution(k, dungeons):
    temp = list(permutations(dungeons, len(dungeons)))
    result = 0

    for i in temp:
        k_temp = k
        cnt = 0
        for j in i:
            if k_temp >= j[0]:
                k_temp -= j[1]
                cnt += 1

        result = max(cnt, result)

    return result




