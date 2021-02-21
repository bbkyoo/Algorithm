x = int(input())

count = 0
lst = [64,32,16,8,4,2,1]



if x in lst:
    count = 1
else:
    for i in lst:  # 이 코드를 사용하면 자동으로 막대기가 알맞은 수를 넣어준다(중요)
        if x >= i:
            x -= i
            count += 1

print(count)
