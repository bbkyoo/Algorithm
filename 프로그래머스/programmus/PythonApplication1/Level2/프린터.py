# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.

# 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities
# 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location
# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

def solution(priorities, location):         
    answer = 0

    arr1 = [c for c in range(len(priorities))]
    arr2 = priorities

    i = 0
    while True:
        if arr2[i] < max(arr2[i+1:]):
            arr1.append(arr1.pop(i))
            arr2.append(arr2.pop(i))
        else:
            i += 1

        if arr2 == sorted(arr2, reverse = True):
            break

    return arr1.index(location) + 1


