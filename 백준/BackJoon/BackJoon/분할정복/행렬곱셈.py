# 파이썬 행렬 곱셈은 N*M 행렬과 M*K 행렬이 만나 N*K행렬을 만든 다는 것만 기억하면 된다.

N, M = map(int, input().split()) 

a_lt = []
for _ in range(N):
    a_lt.append(list(map(int, input().split())))

M, K = map(int, input().split())

b_lt = []
for _ in range(M):
    b_lt.append(list(map(int, input().split())))

result = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            result[n][k] += a_lt[n][m] * b_lt[m][k]     # 곱셈 외우자

for i in result:
    for j in i:
        print(j, end= ' ')
    print()














