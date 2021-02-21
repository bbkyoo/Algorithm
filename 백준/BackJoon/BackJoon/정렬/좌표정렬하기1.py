import sys

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split(" "))
    lst.append([x,y]) # 이차원 리스트에 삽입할때 이렇게 삽입함
    
lst_result = list(set(map(tuple, lst))) # 이차원 리스트 중복제거 알아두기
lst_result.sort()

for i in range(N):
    print('{} {}'.format(lst_result[i][0],lst_result[i][1])) # 리스트 벗길때 유용항 format 출력형식 기억해두기