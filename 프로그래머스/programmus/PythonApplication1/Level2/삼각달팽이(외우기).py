# https://coding-lks.tistory.com/56
# 1. n x n 의 matrix를 만든다
# 2. 그 안에서 아래, 오른쪽, 대각선 왼쪽 별로 num을 1부터 시작하여 계속 증가시키며
# 넣는다.


def solution(n):
    res = [[0]*n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1

    for i in range(n):
        for j in range(i,n):

            # down
            if i % 3 == 0:
                x += 1

            # right
            elif i % 3 == 1:
                y += 1

            # up
            elif i % 3 == 2:
                x -= 1
                y -= 1

            res[x][y] = num
            num += 1

    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)

    return answer
