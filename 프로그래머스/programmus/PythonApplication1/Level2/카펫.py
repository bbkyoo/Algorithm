# 걍 근의 공식으로 x와 y를 찾으면 되는 문제

def solution(brown, yellow):
    x = ((brown+4) + ((brown+4)**2 - 16*(brown+yellow))**0.5  )/4
    y = (brown + yellow) / x

    answer = []
    answer.append(max(x, y))
    answer.append(min(x, y))

    return answer



