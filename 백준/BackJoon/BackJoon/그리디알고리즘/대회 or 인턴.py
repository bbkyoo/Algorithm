n,m,k = map(int, input().split())

result = 0
while n >= 2 and m >= 1 and n + m >= k + 3:	# 2명 , 1명 팀 만들 수 있고, 인턴쉽도 보낼 수 있는 수 일때
    n -= 2	# 빼주고
    m -= 1	# 빼주고
    result += 1	# 팀 수는 하나씩 더해준다
print(result)