N = [list(map(int, input().split())) for i in range(5)]

sum_list = []

for i in range(5):
    sum_list.append(sum(N[i]))

print(sum_list.index(max(sum_list)) + 1,max(sum_list))