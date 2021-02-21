import sys

N = int(sys.stdin.readline())
lst = []
while True:
    lst.append(N%10)
    N = N//10    
    if N == 0:
        break

lst.sort(reverse=True)

for i in lst:
    print(i, end="")    # 이렇게 하면 리스트에서 [ , ] 를 빼고 출력 end ="" 를 기억해라  