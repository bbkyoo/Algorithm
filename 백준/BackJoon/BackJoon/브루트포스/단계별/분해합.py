N = int(input())
init_parts = []
init = 0

for i in range(1,N+1):
    init_parts = list(map(int, str(i))) # 각 자리수 분리 하기 이게 핵심
    if i + sum(init_parts) == N:
        init = i                        
        break    # 어차피 작은 수 부터 올라오기 때문에 이렇게 수를 찾으면 break
    
print(init)