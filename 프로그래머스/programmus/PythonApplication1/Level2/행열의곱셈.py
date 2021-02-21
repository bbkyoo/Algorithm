def solution(arr1, arr2):
    N = len(arr1)
    M = len(arr1[0])

    K = len(arr2)
    L = len(arr2[0])

    result = [[0]*L for _ in range(N)]

    for n in range(N):
        for l in range(L):
            for m in range(M):
                result[n][l] += (arr1[n][m] * arr2[m][l])

    return result

