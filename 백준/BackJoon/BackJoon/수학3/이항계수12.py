import sys

N, K = map(int, sys.stdin.readline().split())

result_n = 1
for i in range(1,N+1):
    result_n = result_n * i

result_k = 1
for i in range(1,K+1):
    result_k = result_k * i

result_nk = 1
for i in range(1,N-K+1):
    result_nk = result_nk * i

end = (result_n)//(result_k * result_nk)

if K < 0 or K > N:
    print(0)
else:
    print(end % 10007)