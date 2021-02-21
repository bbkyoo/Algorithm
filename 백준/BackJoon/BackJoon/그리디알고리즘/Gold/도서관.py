# 음수와 양수를 각각 나눠서 저장한다.
# 나눠서 저장한 각각을 내림차순으로 정렬한다.
# 음수 첫번째와 양수 첫번째 값을 비교해서 작은것부터 가져다 놓는다. (예제에서 보면 39와 11을 비교한것. 11이 더 적으니까 양수부터 가져다 놓는것이다)
# 가져다 놓을때는 멀리있는거부터 m권씩 끊어서 맨앞에 있는 값를 저장한다(39,37 / 29,28 / 6 이런식으로 말이다).
# 걸음 수를 계산할때는 기본적으로 곱하기 2를 해줘야 하지만, 가장 마지막 39는 예외라는 것을 주의해야한다.

# 내가 짠 코드, 런타임 에러

#import sys
#input = sys.stdin.readline

#n, m = map(int, input().split())

#books = list(map(int, input().split()))
#plus = []
#minus = []
#for i in books:
#    if i > 0:
#        plus.append(i)
#    else:
#        minus.append(i)

#plus.sort()
#minus.sort()

#answer = 0

#if abs(plus[-1]) > abs(minus[0]):
#    if len(plus) >= m:
#        answer += plus[-1]
#        for _ in range(m):
#            plus.pop()
#        while plus:
#            answer += (plus[-1] * 2) 
#            for i in range(m):
#                if not plus:
#                    break
#                plus.pop()
#    else:
#        answer += plus[-1]

#    while minus:
#        if len(minus) >= m:
#            answer += (abs(minus[-m]) * 2) 
#            for i in range(m):
#                if not minus:
#                    break
#                minus.pop(-1)
#        else:
#            answer += (abs(minus[0]) * 2)
#            minus.clear()

#else:        
#    if len(minus) >= m:
#        answer += abs(minus[0])
#        for _ in range(m):
#            minus.pop(0)
#        while minus:
#            answer += (abs(minus[0]) * 2) 
#            for i in range(m):
#                if not minus:
#                    break
#                minus.pop(0)              
#    else:
#        answer += minus[0]

#    while plus:
#        if len(plus) >= m:
#            answer += (plus[m-1] * 2) 
#            for i in range(m):
#                if not plus:
#                    break
#                plus.pop(0)
#        else:
#            answer += (plus[m-1] * 2)
#            plus.clear()

#print(answer)

# 정답코드, 우선순위 큐 사용

import heapq

n, m = map(int, input().split())  # 책수, 동시에 들수있는수
array = list(map(int, input().split()))

postive = []
negative = []

# 가장 거리가 먼 책까지의 거리
largest = max(max(array), -min(array))

# 최대 힙을 위해 원소를 음수로 구성
# heapq는 기본적으로 min heap이기 때문
for i in array:
    # 책의 위치가 양수인 경우
    if i > 0:
        heapq.heappush(postive, -i)
    # 책의 위치가 음수인 경우
    else:
        heapq.heappush(negative, i)

result = 0

while postive:
    # 한번에 m개씩 옮길 수 있으므로 m개씩 빼내기
    result += heapq.heappop(postive)
    for _ in range(m - 1):
        if postive:
            heapq.heappop(postive)

while negative:
    # 한번에 m개씩 옮길 수 있으므로 m개씩 빼내기 
    result += heapq.heappop(negative) 
    for _ in range(m - 1):
        if negative:
            heapq.heappop(negative)
            
# 일반적으로 왕복 거리를 계산하지만, 가장 먼 곳은 편도로 계산
print(-result * 2 - largest)





