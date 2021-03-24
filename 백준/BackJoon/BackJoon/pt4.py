a,b,c,d,e = map(float, input().split())

n, m = map(int, input().split())

arr1 = []
for _ in range(n):
    arr1.append(list(input()))

arr2 = []
for _ in range(n):
    arr2.append(list(input()))

arr = []

for i in range(n):
    for j in range(m):
        if arr2[i][j] == "A":
            arr.append([arr1[i][j], arr2[i][j], a, i, j])
        elif arr2[i][j] == "B":
            arr.append([arr1[i][j], arr2[i][j], b, i, j])
        elif arr2[i][j] == "C":
            arr.append([arr1[i][j], arr2[i][j], c, i, j])
        elif arr2[i][j] == "D":
            arr.append([arr1[i][j], arr2[i][j], d, i, j])
        elif arr2[i][j] == "E":
            arr.append([arr1[i][j], arr2[i][j], e, i, j])

result1 = []
for i in range(len(arr)):
    if arr[i][0] == "Y":
        result1.append(arr[i])

if result1:
    result1.sort(key = lambda x : (-x[2] , x[3] , x[4]))

result2 = []
for i in range(len(arr)):
    if arr[i][0] == "O":
        result2.append(arr[i])

if result2:
    result2.sort(key = lambda x : (-x[2] , x[3] , x[4]))

result = result1 + result2

for i in range(len(result)):
    print(result[i][1], result[i][2], result[i][3], result[i][4])
















