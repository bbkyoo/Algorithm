import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

def solve(n):
    cnt = 0
    num = 1

    while True:
        str_num = str(num)
        flag = True
        if len(num) != 1:
            for i in range(1, len(str_num)):
                if int(str_num[i-1]) <= int(str_num[i]):
                    start = str_num[:i-1]
                    mid = str(int(str_num[i-1])+1)
                    end = '0'+ str_num[i+1:]
                    num = int(start + mid + end)
                    flag = False

        if flag:
            cnt += 1
            if cnt == n:
                return num
            num += 1

n = int(input())

if n >= 1023:
    print(-1)
elif n == 0:
    print(0)
else:
    print(solve(n))
