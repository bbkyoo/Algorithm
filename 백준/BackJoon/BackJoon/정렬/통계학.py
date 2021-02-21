import sys
from collections import Counter   # 이거 쓰는것 알아두기

# 산술 평균 구하기
def lst_avg(lst):
    return round(sum(lst) / len(lst))

# 중앙값 구하기
def lst_median(lst):
    return lst[(n // 2)]

# 최빈값 구하기 
def lst_mode(lst):
    mode_dict = Counter(lst) # 이러면 만약 Counter('hello world') 일때 Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    modes = mode_dict.most_common() #  [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)] 이렇게 데이터의 개수가 많은 순으로 정렬된 배열을 리턴
 
    if len(lst) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]
    
    return mod 

# 범위 구하기
def lst_range(lst):
    return (max(lst) - min(lst))


n = int(sys.stdin.readline())

lst = []

for _ in range(n):
    lst.append(int(sys.stdin.readline())) 
lst.sort()

print(lst_avg(lst))
print(lst_median(lst))
print(lst_mode(lst))
print(lst_range(lst))
