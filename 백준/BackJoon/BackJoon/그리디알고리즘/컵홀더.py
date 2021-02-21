# 파이썬에는 변수 선언이 없다.
# 변수 유형에 따라서 초기화하는 방법이 다르다
# a = 0 # int
# b = '0.0' # float
# c = [] #list
# d = () #turple
# e = '' # str
# f = u'' # unicode

N = int(input())

cup = list(map(str, input()))
seat = []
temp = ''

for i in range(N): 
    if cup[i] == 'S':
        seat.append(cup[i])
    else:
        temp += cup[i]
    
    if temp == 'LL':
        seat.append(temp)
        temp = ''

count = 0
for i in range(len(seat)):
    if seat[i] == 'LL':
        count += 1

if count >= 2:
    print(N-(count -1))
else:
    print(N)
























