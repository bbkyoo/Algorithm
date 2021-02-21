N = int(input())

num = list(map(int, input().split()))
add, sub, mul,div = map(int, input().split()) 
    
max_math = -1e9
min_math = 1e9
def dfs(i, res , add , sub , mul , div):
    global max_math, min_math
    if i == N:
        max_math = max(res, max_math)
        min_math = min(res, min_math)
        return
    else:
        if add:
            dfs(i+1, res+num[i], add-1, sub, mul, div)
        if sub:
            dfs(i+1, res-num[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, res*num[i], add, sub, mul-1, div)
        if div:
            dfs(i+1, int(res/num[i]), add, sub, mul, div-1)

dfs(1, num[0], add, sub, mul, div)
print(max_math)
print(min_math)