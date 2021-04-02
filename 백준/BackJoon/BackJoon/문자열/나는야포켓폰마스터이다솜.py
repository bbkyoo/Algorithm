# dic에서 key값과 value 값을 찾을 때 둘다 반대로 저장해 보면 key값과 value값 찾기가 수원하다.
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}
for i in range(1,n+1):
    temp = input().rstrip()
    dic[temp] = str(i)
    dic[str(i)] = temp

for i in range(m):
    temp = input().rstrip()
    if temp in dic:
        print(dic[temp])
    