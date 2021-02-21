N = int(input())

score = [int(input()) for _ in range(N)]

count = 0
for i in range(N-1,0,-1): # 왜 역순을 했는지를 생각
    if score[i-1] >= score[i]:
        count += (score[i-1] - score[i] + 1) # 이 부분이 중요 점수의 차이만큼 더해주고 1차이가 나니까 1을 더해준다 
        score[i-1] = score[i] - 1

print(count)