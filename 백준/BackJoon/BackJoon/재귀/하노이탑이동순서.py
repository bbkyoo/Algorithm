# https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-python-11729%EB%B2%88-%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%91-%EC%9D%B4%EB%8F%99-%EC%88%9C%EC%84%9Chanoi-top-in-python
# n이 짝수 일때는 1번 원판을 2번원판으로 이동
# n이 홀수일 때는 1번 원판을 3번원판으로 먼저 이동 

# 2번 원판을 3으로 옮기기 위해서는 1번 원판이 2에 있어야 하며
# 2번 원판을 3으로 옮긴 후
# 다시 1번을 3으로 옮긴다
# function f:
# f(1번 원판, 1 -> 2)
# 2번 원판 1 -> 3
# f(1번 원판, 2 -> 3) 

n = int(input())

def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)

sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1

print(sum)
hanoi(n, 1, 2, 3)