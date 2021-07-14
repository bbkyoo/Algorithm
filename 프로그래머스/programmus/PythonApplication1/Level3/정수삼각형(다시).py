def solution(triangle):
    k = 2

    for i in range(1,len(triangle)):
        for j in range(k):
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j]
            elif j == i:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
            else:
                triangle[i][j] = triangle[i][j] + max(triangle[i-1][j],triangle[i-1][j-1])
        k += 1

    return max(triangle[-1])