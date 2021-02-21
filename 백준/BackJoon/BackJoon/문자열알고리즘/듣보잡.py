import sys

input = sys.stdin.readline

n, m = map(int, input().split())

liten = []
see =[]
for _ in range(n):
    liten.append(input())
for _ in range(m):
    see.append(input())

result = list(set(liten) & set(see)) 

print(len(result))
result.sort()
for i in result:
    print(i, end='')
