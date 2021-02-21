import sys

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split(" "))
    lst.append([x,y]) # 이차원 리스트에 삽입할때 이렇게 삽입함
    
lst_result = list(set(map(tuple, lst))) # 이차원 리스트 중복제거 알아두기

lst_result.sort(key=lambda x : (x[1], x[0]))

for i in range(N):
    print('{} {}'.format(lst_result[i][0],lst_result[i][1])) # 리스트 벗길때 유용항 format 출력형식 기억해두기

    # a = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]

    # key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다. 
    # c = sorted(a, key = lambda x : x[0]) 
    # c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)] 
    # d = sorted(a, key = lambda x : x[1]) 
    # d = [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]


