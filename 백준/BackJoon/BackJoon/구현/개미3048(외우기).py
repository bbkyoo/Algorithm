import sys
import itertools

input = sys.stdin.readline

n1, n2 = map(int, input().split())
first = list(' '.join(list(input().rstrip()[::-1])))
second = list(' '.join(list(input().rstrip())))
t = int(input())

second = [' ']*len(first) + second + [' ']*len(first)
first = [' ']*t*2 + first

for i in itertools.zip_longest(first, second, fillvalue=' '):
    i = ''.join(i).strip()
    if i:
        print(i, end='')
    
