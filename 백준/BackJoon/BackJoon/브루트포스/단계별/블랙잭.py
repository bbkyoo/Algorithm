N, M = map(int,input().split()) 
sum = 0
cardList = list(map(int,input().split())) 

for i in range(N-2): # 이렇게 분리하여 반복문을 사용하는 것이 포인트
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if cardList[i] + cardList[j] + cardList[k] > M: # 이 continue 활용도 포인트
                continue
            else:
                sum = max(sum, cardList[i] + cardList[j] + cardList[k])                
 
print(sum)
