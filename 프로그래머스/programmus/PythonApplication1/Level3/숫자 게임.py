# 정렬을 하면 더 시간을 줄일수 있다는 교훈을 얻게 되었따.

def solution(A, B):
    ans = 0
    A.sort(reverse=True)
    B.sort(reverse=True)

    for i in A:
        mn = i
        for j in range(len(B)):
            if mn < B[j]:
                mn = B[j]
            else:
                break

        if mn == i:
            continue
        else:
            B.remove(mn)
            ans += 1

    return ans
