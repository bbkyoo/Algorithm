n = int(input())
arr = sorted(list(map(int, input().split())))
temp = []
for i in range(n):
    temp.append(arr[i]+arr[-1-i])

temp.sort()
print(temp[0])