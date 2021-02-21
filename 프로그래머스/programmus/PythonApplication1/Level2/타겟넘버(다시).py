def solution(numbers, target):
    n = len(numbers)
    cnt = 0
    def dfs(L, total):
        if L == n:
            if total == target:
                nonlocal cnt # 현재 함수의 바깥쪽에 있는 지역 변수의 값을 변경하려면 nonlocal 키워드를 사용해야 한다.
                cnt += 1
        else:
            dfs(L+1, total+numbers[L])
            dfs(L+1, total-numbers[L])
    
    dfs(0,0)
    return cnt

numbers = [1,1,1,1,1]
target = 3

print(solution(numbers, target))