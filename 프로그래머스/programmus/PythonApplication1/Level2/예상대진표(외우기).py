# 어렵게 생각 ㄴㄴ
# +1을 해주는 이유는 1 과 2 이면 0 1 이 되므로 이런것을 고려해 준 것

def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1

        a, b = (a+1)//2, (b+1)//2
    
    return answer


