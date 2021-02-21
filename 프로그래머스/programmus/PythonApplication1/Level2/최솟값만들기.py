def solution(A,B):
    A.sort()
    B.sort(reverse=True)

    n = len(A)
    sum = 0
    for i in range(n):
        sum += A[i] * B[i]

    return sum


