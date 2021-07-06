# 1. 그리디란
# 최적의 해에 가까운 값을 구하기 위해 사용됨
# 여러 경우중 하나를 결정해야할 떄마다, 매순간 최적이라고 생각되는 경우를 선택하는 방식으로 진행해서, 최종적인 값을 구하는 방식 

# 2. 탐욕 알고리즘 예

# 문제1. 지불해야 하는 값이 4720 일 때 1원 50 100원 500원 동전으로 동전의 수가 가장 적게 지불하시오.

coin = [500,100,50,1]

def min_coin_count(value, coin):
    count = 0
    
    coin.sort(reverse = True)

    i = 0
    while value > 0:
        count += value // coin[i]
        value %= coin[i]
        i += 1
    return count

# 문제2. 부분 배낭 문제
# 무게 제한이 k인 배낭에 최대가치를 가지도록 물건을 넣는 문제

data_list = [(10,10),(15,12),(20,10),(25,8),(30,5)]# (무게, 가치)

def get_max_value(data_list, capacity):
    data_list.sort(key=lambda x: x[1]/x[0], reverse=True)
    total_value = 0
    details = []

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0],data[1],1])
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            break

    return total_value

print(get_max_value(data_list, 30))

# 3. 그리디의 한계
# 근사치 추정의 활용
# 반드시 최적의 해를 구할 수 있는 것은 아니기 때문
