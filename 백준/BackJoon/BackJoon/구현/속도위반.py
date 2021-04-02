n, m = map(int, input().split())

doro = [[0,0] for _ in range(100)]

start = 0
for _ in range(n):
    o_length, o_limit = map(int, input().split())
    for i in range(start, start + o_length):
        doro[i][0] = i
        doro[i][1] = o_limit

    start += o_length

person = [[0,0] for _ in range(100)]

start = 0
for _ in range(m):
    p_length, p_limit = map(int, input().split()) 
    for i in range(start, start + p_length):
        person[i][0] = i
        person[i][1] = p_limit

    start += p_length

result = 0
for i in range(100):
    if doro[i][1] - person[i][1] >= 0:
        continue
    else:
        result = max(result, person[i][1] - doro[i][1])

print(result)