# 문자열을 정렬시키면 ['911', '97625999', '91125426'] 이런식으로 사전순으로 정렬되므로 비교해줄때 
# i번째와 i+1번째만 비교(붙어있는 문자열끼리만 비교해도 접두어가 겹치는지 알수있음)합니다. 

t = int(input())

def check():
    for i in range(len(a)-1):
        if a[i] == a[i+1][0:len(a[i])]: # [0:len(a[i])] 이것은 어떻게 쓰는 것일까?
            return 'NO' 
    return 'YES'

for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        a.append(input().strip())
    a.sort()
    print(check())

