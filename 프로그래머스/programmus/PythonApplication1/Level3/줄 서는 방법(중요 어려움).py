# https://velog.io/@ansrjsdn/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level3-%EC%A4%84-%EC%84%9C%EB%8A%94-%EB%B0%A9%EB%B2%95-Python

import math

def solution(n, k):
    answer = []
    arr = [i for i in range(1, n+1)]

    while n != 0:
        temp = math.factorial(n-1)
        index = k // temp
        k = k % temp

        if k == 0:
            answer.append(arr.pop(index-1))
        else:
            answer.append(arr.pop(index))

        n -= 1

    return answer