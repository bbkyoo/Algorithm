def solution(n, m):
    
    N, M = n, m

    while m != 0:
        n = n % m
        n, m = m, n
    
    answer = []

    answer.append(n)
    answer.append((N*M)//n)
        
    return answer
