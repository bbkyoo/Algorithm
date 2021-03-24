bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))

num = list(map(int, input().split()))
for _ in range(4):
    num += list(map(int, input().split()))

check = [0] * 12 #바뀐것의 갯수 저장하는 리스트 idx0~4는 row / 5~9는 col / 10, 11은 대각
line = 0
flag = False

count = 0
for n in range(25):
    if flag == True:
        break
    for i in range(5):
        if flag == True:
            break
        for j in range(5):
            if flag == True:
                break
            if num[n] == bingo[i][j]:
                bingo[i][j] = 0
                check[i] += 1
                check[j+5] += 1
                if i == j: # 대각
                    check[10] += 1
                if i + j == 4: # 반대 대각
                    check[11] += 1
                 
                for c in range(12):
                    if check[c] == 5:
                        check[c] = 0
                        line += 1
                        if line == 3:
                            flag = True
                            break
    count += 1

print(count)
















