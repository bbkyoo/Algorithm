import sys

n, k = map(int, input().split())
doll = list(map(int, input().split()))

mn = float('inf')

while (k != (n+1)): # 이렇게 인덱스를 늘리는 것이 더 정확도가 높다
    full_range = n - k + 1

    for i in range(full_range):
        do_list = doll[i: i+k]
        mean = sum(do_list) / k
        var = sum ([(x-mean)**2 for x in do_list]) / k
        std = var**0.5
        mn = min(mn, std)
    k += 1  # 이렇게 인덱스를 늘리는 것이 더 정확도가 높다

sys.stdout.write(str(mn))


