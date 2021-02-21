# 자연수 n을 연속한 자연수들로 표현 하는 방법

def solution(n):
    count = 1 
    for i in range(1, (n+1)//2 + 1):
        sum = 0
        for j in range(i, (n+1)//2 + 1):
            sum += j
            if sum == n:
                count += 1
                break
            elif sum > n: # 완전탐색으로 시간초과가 날때는 이런 문장으로 시간을 줄여보기
                break    

    return count
        