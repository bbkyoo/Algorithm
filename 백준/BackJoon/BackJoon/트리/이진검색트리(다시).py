# 이진 검색 트리는 다음과 같은 세 가지 조건을 만족하는 이진 트리이다.
# - 노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
# - 노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
# - 왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.

import sys
sys.setrecursionlimit(10 ** 6)

def post_order(start, end):
    if start > end:
        return

    division = end + 1

    for i in range(start+1, end+1):
        if pre_order[start] < pre_order[i]:
            division = i
            break

    # 왼쪽 서브트리
    post_order(start+1, division-1)
    # 오른쪽 서브트리
    post_order(division, end)
    # 후위순회 이므로 제일 마지막에 찍는다
    print(pre_order[start])

pre_order = []
count = 0
while count <= 10000:
    try:
        pre_order.append(int(input()))
    except:
        break
    count += 1

post_order(0, len(pre_order)-1)





