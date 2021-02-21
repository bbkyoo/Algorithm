import string
import sys

N = sys.stdin.readlines()

lst =list(string.ascii_lowercase) # 리스트 만드는 방법
count = []
for i in range(len(lst)):
    count.append(0)

for i in range(len(N)):
    if N[i] in lst:
        count[lst.index(N[i])] += 1

for i in range(len(count)):
    if count[i] == max(count):
        print(lst[i], end="")