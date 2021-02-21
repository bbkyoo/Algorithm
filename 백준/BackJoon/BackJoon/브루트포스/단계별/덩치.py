def rankOfSize(num):
    sizeList = [list(map(int,input().split())) for _ in range(num)] # 이렇게 입력 받는거 기억 -> 이 중 리스트 받기 
    rankList = []
    for i in range(num):
        rank = 1                        # 이 줄부터
        for j in range(num):
            if sizeList[i][0] < sizeList[j][0] and sizeList[i][1] < sizeList[j][1]:
                rank += 1
        rankList.append(str(rank))           # 여기까지 핵심
    
    return rankList

N = int(input())
print(" ".join(rankOfSize(N)))

