n, k = map(int, input().split())

tall = list(map(int, input().split()))
res = []
for i in range(1, len(tall)):
    res.append([tall[i] - tall[i-1], i])

res.sort(reverse=True)

asdf    