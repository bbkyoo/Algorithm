# https://velog.io/@good159897/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Python-%EB%89%B4%EC%8A%A4-%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%EB%A7%81 보기

def solution(str1, str2):
    list_str1 =[]
    list_str2 =[]

    for s1, slice_s1 in zip(str1, str1[1:]):
        join_str = "".join([s1, slice_s1])
        if join_str.isalpha():
            list_str1.append(join_str.lower())

    for s2, slice_s2 in zip(str2, str2[1:]):
        join_str = "".join([s2, slice_s2])
        if join_str.isalpha():
            list_str2.append(join_str.lower())

    # 교집합의 갯수
    if len(list_str1) > len(list_str2):
        inter = [list_str1.remove(x) for x in list_str2 if x in list_str1]
    else:
        inter = [list_str2.remove(x) for x in list_str1 if x in list_str2]

    # 합집합은 교집합 + 나머지 원소들

    list_uni = list_str1 + list_str2
    uni = len(list_uni)

    if uni == 0:
        return 65536
    else:
        return int(len(inter)/uni * 65536)


















