# p 로봇, h 부품
n, k = map(int, input().split())
arr = list(input())

for i in range(n):
    isTrue = True
    if arr[i] == 'P':
        if 0 <= i-k and isTrue:
            for j in range(i-k,i):
                if arr[j] == 'H':
                    arr[j] = 'C'
                    isTrue = False
                    break
        if i+k < n and isTrue:
            for j in range(i+1,i+1+k):
                if arr[j] == 'H':
                    arr[j] = 'C'
                    break

print(arr.count("C"))
