def solution(strings, n):
    
    answer = sorted(sorted(strings), key=lambda x : x[n]) # 이거 두번 오름차순 하는거 중요

    return answer

