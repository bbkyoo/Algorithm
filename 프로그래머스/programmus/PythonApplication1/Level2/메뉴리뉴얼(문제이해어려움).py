from itertools import combinations

# 여기서 중요한 것은 예제3의 WX의 경우인데 이 것은 처음에 orders를 정렬해주면 해결된다.
# 그 이유는 모든 값은 사전 순으로 넣어줘야 하기 때문이다.

def solution(orders, course):
    dic = {} 
    for i in range(len(orders)):
        for j in course:
            temp = list(set((combinations(sorted(orders[i]),j))))
            for k in temp:
                if k not in dic:
                    dic[k] = 1
                else:
                    dic[k] += 1

    answer = []

    for i in course:
        mx = 0
        for j in dic.keys():
            if len(j) == i:
                if mx <= dic[j]:
                    mx = dic[j]

        for k in dic.keys():
            if len(k) == i:
                if dic[k] == mx and dic[k] >= 2:
                    answer.append(''.join(k))

    return sorted(answer)

print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))


