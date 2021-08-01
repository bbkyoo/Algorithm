import time
from itertools import permutations

start = time.time()
k = 9
m = 1

arr = []
for i in range(1, k+1):
    arr.append(i)

lt = []
for i in list(set(permutations(arr, k))):
    temp = ''
    for j in i:
        temp += str(j)
    lt.append(int(temp))

