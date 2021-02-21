N = int(input())

result = 0
for i in range(N):
    a ,b, c, d = map(int, input().split())
    lists = ['a','b','c','d']
    cnts = dict()

    for li in lists:
        if li not in cnts.keys():
            cnts[li] = 1
        else:
            cnts[li] += 1
    print(cnts)
