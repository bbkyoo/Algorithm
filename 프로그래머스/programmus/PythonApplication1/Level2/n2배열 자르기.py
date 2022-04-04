# 시간초과
# def solution(n, left, right):
#     matrix = [[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(i+1):
#             matrix[i][j] = i + 1
#             matrix[j][i] = i + 1
#
#     arr = []
#     for i in matrix:
#         for j in i:
#             arr.append(j)
#
#     return arr[left:right+1]


# 느낀점... 패턴을 찾고 문제를 풀어야 시간초과를 없앨 수 있다.
# https://velog.io/@hannahf97/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-n2-%EB%B0%B0%EC%97%B4-%EC%9E%90%EB%A5%B4%EA%B8%B0
def solution(n, left, right):
    answer = []
    for i in range(int(left), int(right+1)): # 이거 int로 감싸지 않으면 런타임 에러가 발생한다.
        a = i//n
        b = i%n
        if a < b:
            a, b = b, a
        answer.append(a+1)
    return answer






