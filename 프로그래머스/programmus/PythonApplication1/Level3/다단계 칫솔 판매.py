#def solution(enroll, referral, seller, amount):
#    answer = []
#    return answer

# https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-2021-Dev-Matching-%EB%8B%A4%EB%8B%A8%EA%B3%84-%EC%B9%AB%EC%86%94-%ED%8C%90%EB%A7%A4

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10] 

tree = {'-':'root'}
sell = {'-': 0}

for i in range(len(enroll)):
    child = enroll[i]
    parent = referral[i]
    sell[child] = 0
    tree[child] = parent

for i in range(len(seller)):
    child = seller[i]
    parent = tree[child]
    money = amount[i] * 100
    sell[child] += money

    while True:
        commision = money // 10
        sell[child] -= commission
        sell[parent] += commision
        child = parent
        parent = tree[child]
        money = commission
        if parent == 'root':
            break

ans = []
for person in enroll:
    ans.append(sell[person])

print(ans)







