N = int(input())
lt = []

for _ in range(N):
    lt.append(int(input()))

# c++ 적인 풀이
#for i in range(N):
#    for j in range(i+1,N):
#        if lt[i] > lt[j]:
#            temp = lt[i]
#            lt[i] = lt[j]
#            lt[j] = temp
#for k in lt:
#    print(k)   


# 파이썬 적인 풀이
#lt.sort()
#for k in lt:
#    print(k)