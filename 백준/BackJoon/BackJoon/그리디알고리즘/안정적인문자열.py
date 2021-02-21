#문제해결 IDEA 
#- 왼쪽 괄호('{') 를 저장하는 Stack을 맏듭니다.
#- 오른쪽 괄호가 나왔을때 왼쪽 괄호 stack을 pop 합니다. stack이 비어있을 경우 Count를 1 더하고 왼쪽 괄호 Stack에 '{'를 적재합니다.
#- 문자열을 끝까지 탐색한 후 왼쪽 괄호 Stack이 비어있지 않는다면 Stack의 길으를 2를 나눈 값을 Count에 더해주면 정답입니다.

s = []
while True:
    temp = input()

    if '-' in temp:
        break

    s.append(temp)

for i in range(len(s)):
    q = []
    cnt = 0
    for j in range(len(s[i])):
        if s[i][j] == '{':
            q.append(s[i][j])
        else:
            if q:
                q.pop()
            else:
                cnt += 1
                q.append("{")

    if q:
        cnt += len(q)//2

    print('{}. {}'.format(i+1, cnt))