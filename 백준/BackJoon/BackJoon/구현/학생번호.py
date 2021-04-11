n = int(input())

arr = []
for _ in range(n):
    arr.append(input()[::-1])

isTrue = False
k = 1
while True:
    if isTrue:
        break

    temp = []
    for i in range(len(arr)):
        temp.append(arr[i][:k])

    isTrue = True
    for i in range(len(temp)):
        if isTrue == False:
            break
        for j in range(i+1, len(temp)):
            if temp[i] == temp[j]:
                isTrue = False
                break
    k += 1

print(k-1)