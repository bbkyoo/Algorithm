# 내가 만든 시긴초과코드

#def solution(phone_book):
#    answer = True

#    phone_book.sort(key = lambda x : len(x))

#    for i in range(len(phone_book)):
#        for j in range(i+1, len(phone_book)):
#            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                answer = False
#                break
#    return answer

# 이 풀이는 살펴보기
#def solution(phone_book):
#    phone_book.sort()
#    for p1, p2 in zip(phone_book, phone_book[1:]):
#        if p2.startswith(p1):
#            return False
#    return True


def solution(phone_book):
    phone_book.sort() # 이 부분에서 phone_book = ["12","123","1235","567","88"] 이런 문자열 배열을 정렬했을때 나오는 값을 보면 ["12","123","1235","567","88"] 이런 형식이란 것을 기억하고 풀기
    for a in range(len(phone_book)-1):
        if phone_book[a] in phone_book[a+1] :
            return False
    return True























