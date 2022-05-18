# 문제 이해부터 제대로 하자
# 문제 이해력이 가장 중요한 문제
# citations = [20,19,18,1] 이라 할때 답은 3이다 왜 일까? 논문 4편중 3번이상 인용된 논문이 3편(20,19,18) 나머지 논문이 3번 이하(1) 인용되었기 때문이다. 

def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

print(solution([3, 0, 6, 1, 5]))