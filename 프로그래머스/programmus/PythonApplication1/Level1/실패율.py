#실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

#def solution(N, stages):
#    stages.sort()

#    arr = []
#    for i in range(1, N+1):
#        temp_element = 0
#        temp_total = 0
#        for j in range(len(stages)):
#            if stages[j] == i:
#                temp_element += 1
#            if stages[j] >= i:
#                temp_total += 1
#        if temp_element != 0:
#            arr.append(temp_element/temp_total)
#        else:
#            arr.append(0)

#        answer = []

#    for i, j in enumerate(arr):
#        answer.append((i+1,j))

#    answer = sorted(sorted(answer, key = lambda x : x[0]), key = lambda x : x[1], reverse=True)
#    result = []
#    for i in range(len(answer)):
#        result.append(answer[i][0])
    
#    return result

def solution(N, stages):
    k = len(stages)
    s = []
    for i in range(1, N+1):
        c = 0
        for j in range(len(stages)):
            if stages[j] == i:
                c += 1
        if c == 0:
            s.append(0)
        else:
            s.append(c/k)
        k = k - c

    a = sorted(s, reverse=True) # 이 부분부터가 제일 중요
    answer = []

    for i in range(len(a)):
        answer.append(s.index(a[i])+1)
        s[s.index(a[i])] = 2
        print(s)
    return answer




