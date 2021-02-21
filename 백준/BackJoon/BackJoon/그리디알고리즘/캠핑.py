# 캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다. 
# 강산이는 이제 막 V일짜리 휴가를 시작했다. 
# 강산이가 캠핑장을 최대 며칠동안 사용할 수 있을까? (1 < L < P < V)

i = 1
while True:
    L, P, V = map(int, input().split())
    
    if L == 0 and P == 0 and V == 0:
        break

    count = 0
    while V:
        if V < P:
            if V < L:
                count += V
                V = 0
                
            else:
                count += L
                V = 0
                
        else:
            V -= P
            count += L
    
    print("Case {}: {}".format(i ,count))
    i += 1