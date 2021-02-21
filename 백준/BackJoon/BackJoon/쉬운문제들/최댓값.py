num = []

for i in range(9):
    num.append(list(map(int,input().split())))

num_max = []
row_idx = 0
col_idx = 0

for i in range(9):
    num_max.append(max(num[i]))

for i in range(9):
    for j in range(9):
        if max(num_max) == num[i][j]:
            row_idx = i + 1
            col_idx = j + 1

print(max(num_max))
print(row_idx,col_idx)