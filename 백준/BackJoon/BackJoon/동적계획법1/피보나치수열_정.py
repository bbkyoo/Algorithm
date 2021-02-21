import sys

zero = [1, 0]
one = [0, 1]

def fivonacci(n):
    if n <= 1:
        return 
    
    for i in range(2,n+1):
        zero.append(zero[i-1] + zero[i-2])
        one.append(one[i-1] + one[i-2])

    return zero, one

fivonacci(40)

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    print(zero[n], one[n])
               
