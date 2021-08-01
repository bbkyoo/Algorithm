def solution(numbers, target):
    result = 0

    def dfs(i, res):
        nonlocal result
        if i == len(numbers):
            if res == target:
               result += 1
            return
        else:   
            dfs(i+1,res+numbers[i])
            dfs(i+1,res-numbers[i])

    dfs(0, 0)

    return result
