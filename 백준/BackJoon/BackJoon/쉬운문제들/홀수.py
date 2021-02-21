num_list = []

for i in range(7):
    N = int(input())
    if (N % 2) == 1:
        num_list.append(N)

if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))
