#우리는 이분 탐색으로 어떤 수보다 작은 자연수의 곱(i * j)이 몇 개인지 알아낼 것이다.
#A보다 작은 숫자가 몇개인지 찾아내면 A가 몇 번째 숫자인지 알 수 있다.(너무나 당연)

#예를 들어 10 * 10에서 20보다 작거나 같은 수를 생각해보자.
#1*1~1*10
#2*1~2*10
#3*1~3*6
#.
#.
#.

#10*1~10*2
#위 수가 존재할텐데, 이는 반대로 생각해보면 20을 행으로 나눈 몫이다.
#20//1: 10개 --> 단 열의 숫자(N*N배열이므로)를 초과할 수 없다.
#20//2: 10개
#20//3: 6개
#.
#.
#.
#20//10: 2개
#따라서 이를 식으로 표기해보면 아래와 같다.

#temp = 0
#for i in range(1, N+1):
#        temp += min(mid//i, N)

import sys

input = sys.stdin.readline

N = int(input())
k = int(input())

low = 0
high = k
while low <= high:
    mid = (low + high) //2
    count = 0
    for i in range(1, N+1):
        count += min(mid//i, N)

    if count < k:
        low = mid + 1
    else:
        high = mid - 1
        answer = mid

print(answer)
