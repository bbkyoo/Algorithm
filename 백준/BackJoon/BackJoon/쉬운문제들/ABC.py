temp = list(map(int, input().split()))
temp.sort()
A = temp[0]
B = temp[1]
C = temp[2]

result = input()
for i in range(len(result)):
    if result[i] == 'A':
        print(A, end=" ")
    elif result[i] == 'B':
        print(B, end=" ")
    else:
        print(C, end=" ")
