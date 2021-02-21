from collections import deque

N, K = map(int,input().split())

nums = deque(list(i for i in range(1,N+1)))
st =[]

while nums:
    nums.rotate(-(K-1)) # 맨 왼쪽으로 보내고
    st.append(nums.popleft()) # 그 것을 빼면서 추가한다.

print('<' + ', '.join(map(str, st))+'>')
