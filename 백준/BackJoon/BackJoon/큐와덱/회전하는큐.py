from collections import deque

n, m = map(int, input().split())
s = list(map(int, input().split()))
q = deque([])
for i in range(1,n+1):
    q.append(i)

cnt = 0
for i in range(m):
    q_len = len(q)
    q_index = q.index(s[i])

    if q_index < q_len - q_index: # 절반보다 인덱스가 작다면
        while True:
            if q[0] == s[i]:
                q.popleft()
                break
            else:
                q.rotate(-q_index)
                cnt += q_index
    else:
        while True: # 절반보다 인덱스가 크다면
            if q[0] == s[i]:
                q.popleft()
                break
            else:
                q.rotate(q_len - q_index)
                cnt += (q_len - q_index)

print(cnt)