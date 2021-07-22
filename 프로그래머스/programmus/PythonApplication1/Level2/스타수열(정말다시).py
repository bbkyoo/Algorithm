# https://inspirit941.tistory.com/316

from collections import Counter
# Counter을 사용하여 a 리스트의 요소 갯수를 dict형태로 내림차순으로 찾아낸다.

def solution(a):
    elements = Counter(a)
    answer = -1

    # k를 기준으로 스타수열을 만들 수 있는지 확인.
    for k in elements.keys():
        # k의 등장횟수가 스타수열에 사용된 공통인자 횟수보다 작거나 같으면
        # 더 계산할 필요가 없으므로
        if elements[k] <= answer:
            continue

        common_cnt = 0
        idx = 0

        while idx < len(a)-1:
            # a[idx]와 a[idx+1] 둘 다 k가 없는 경우: 공통값 k가 없다.
            # a[idx] == a[idx+1]인 경우: 조건에 위배
            if (a[idx] != k and a[idx+1] != k) or (a[idx] == a[idx+1]):
                idx += 1
                continue

            # 스타 원소로 추가할 수 있는 경우, k 원소가 사용된 횟수를 1 증가시킨다.
            common_cnt += 1
            # 다음 배열 탐색을 위해서는, idx를 2 증가시킨다. 
            idx += 2

        answer = max(common_cnt, answer)

    if answer == -1:
        return 0
    else:
        return answer * 2
