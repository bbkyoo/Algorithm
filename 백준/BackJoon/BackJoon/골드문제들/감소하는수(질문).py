import sys

input = sys.stdin.readline

n = int(input())

count = -1
answer = -1

def solution(limit, sub):
    global count
    global answer

    if len(sub) == limit:
        count += 1

        # count가 n과 같아지는 순간 숫자를 출력하고 종료한다.
        if count == n:
            answer = int(sub)
            print(answer)
            sys.exit()
        return
    
    else:
        # 가장 처음일 경우 맨앞자리 숫자를 limit-1 부터 0까지로 만든다.

        if sub == '':
            for i in range(limit-1, 10):
                sub += str(i)
                solution(limit, sub)
                sub = ''
        else:
            for i in range(int(sub[-1])):
                if limit - len(sub) - 1 > i:
                    continue
                sub += str(i)
                solution(limit, sub)
                sub = sub[:-1]

for k in range(1, 11):
    solution(k, '')
print(-1)



