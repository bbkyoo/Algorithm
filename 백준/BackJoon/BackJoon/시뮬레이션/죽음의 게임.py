n, k = map(int, input().split())

matrix = [] 
for i in range(n):
    matrix.append(int(input()))

a = matrix[0]

mylist = []

for _ in range(len(matrix)):
    mylist.append(a)
    b = matrix[a]
    mylist.append(b)
    a = matrix[b]
    
if k in mylist:
    print(mylist.index(k) + 1)
else:
    print('-1')