from collections import defaultdict

def solution(id_list, report, k):
    limit_list = []

    dic = defaultdict()
    dic2 = defaultdict()

    report = set(report)

    for i in id_list:
        dic[i] = 0
        dic2[i] = 0

    for i in report:
        temp = i.split()
        dic2[temp[1]] += 1

    for i, v in dic2.items():
        if v >= k:
            limit_list.append(i)

    for i in report:
        temp = i.split()
        if temp[1] in limit_list:
            dic[temp[0]] += 1

    result = []
    for v in dic.values():
        result.append(v)

    return result