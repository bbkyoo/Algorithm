def solution(price, money, count):
    price_sum = 0
    for i in range(1 ,count+1):
        price_sum += price * i

    if price_sum - money > 0:
        answer = price_sum - money
    else:
        answer = 0

    return answer
