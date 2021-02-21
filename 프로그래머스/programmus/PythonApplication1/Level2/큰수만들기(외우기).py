def solution(number, k):
    number = list(number)
    n = len(number)
    tk = k
    dp = []

    for i in range(len(number)):
        while tk > 0 and dp and dp[-1] < number[i]: # 여기 코드는 무조건 외우기
            del dp[-1]
            tk -= 1
        dp.append(number[i])
    
    return ''.join(dp[:n-k]) # 이걸 꼭 해줘야 함, 아니면 반례가 있을 수 있다. 

