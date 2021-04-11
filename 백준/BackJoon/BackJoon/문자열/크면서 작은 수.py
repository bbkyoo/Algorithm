import sys
import copy
from itertools import permutations

input = sys.stdin.readline

x = list(map(int, input().rstrip()))
ori = ''

for i in x:
    ori += str(i)
ori = int(ori)

x_mx = sorted(x, reverse=True)
x_tp = copy.deepcopy(x)

answer = 999999
if x == x_mx:
    print(0)
else:
    temp = list(set(permutations(x, len(x_tp))))
    for i in temp:
        result = ''
        for j in i:
            result += str(j)
        
        if int(result) > ori:
            answer = min(int(result), answer)

    print(answer)

        

            