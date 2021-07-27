# https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-2021-Dev-Matching-%EB%8B%A4%EB%8B%A8%EA%B3%84-%EC%B9%AB%EC%86%94-%ED%8C%90%EB%A7%A4

# 시간초과 코드 하지만 알아둘 것

#def solution(enroll, referral, seller, amount):
#    tree = {'-':'root'}
#    sell = {'-': 0}

#    for i in range(len(enroll)):
#        child = enroll[i]
#        parent = referral[i]
#        sell[child] = 0
#        tree[child] = parent

#    for i in range(len(seller)):
#        child = seller[i]
#        parent = tree[child]
#        money = amount[i] * 100
#        sell[child] += money

#        while True:
#            commision = money // 10
#            sell[child] -= commision
#            sell[parent] += commision
#            child = parent
#            parent = tree[child]
#            money = commision
#            if parent == 'root':
#                break

#    ans = []
#    for person in enroll:
#        ans.append(sell[person])

#    return ans

def find(parents, money, number, answer):
    if parents[number] == number or money // 10 == 0:
        answer[number] += money
        return
    send = money // 10
    mind = money - send
    answer[number] += mine
    find(parents, send, parents[number], answer)
    return

def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = [0] * (n+1)

    d = {}
    parents = [i for i in range(n+1)]
    
    for i in range(n):
        d[enroll[i]] = i + 1

    for i in range(n):
        if referral[i] == '-':
            parents[i+1] = 0
        else:
            parents[i+1] = d[referral[i]]

    for i in range(len(seller)):
        find(parents, amount[i]*100, d[seller[i]], answer)

    return answer[1:]
