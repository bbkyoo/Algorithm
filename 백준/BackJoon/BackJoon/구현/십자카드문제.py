import sys

input = sys.stdin.readline

def rotate(arr, n): # 배열 회전시키는 함수
    if not arr:
        return arr
    
    n %= len(arr)
    if not n:
        return arr

    left = arr[:-n]
    right = arr[-n:]

    return right + left

card = list(map(int, input().split()))
card_list = []

for i in range(4):
    temp = rotate(card, i)
    s = ''
    for j in temp:
        s += str(j)
    card_list.append(int(s))

watch = min(card_list)

count = 0
arr = [] 
for i in range(1111,10000):
    if i == watch:
        break

    tp = list(str(i))
    isTrue = True
    if '0' in tp:
        continue
    
    for j in range(4):
        if rotate(tp, j) in arr:
            isTrue = False
            break

    if isTrue:
        arr.append(list(str(i)))
        count += 1
    else:
        continue

print(count+1)





















