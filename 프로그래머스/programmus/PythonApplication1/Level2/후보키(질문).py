#def solution(relation):
#    answer = 0
#    return answer

from itertools import combinations

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

answer = 0

# 모든 컬럼의 조합 리스트
all = list()

# 유일성 만족하는 조합 리스트
uniqeIndex = []

if len(relation) > 0:
    # 컬럼의 개수
    colSize = len(relation[0])

    # 로우의 개수
    rowSize = len(relation)

    # 모든 컬럼의 조합 구하기 (set형태)
    for i in range(1, colSize + 1):
        all.extend([set(k) for k in combinaions([j for j in range(colSize)], i)])
 