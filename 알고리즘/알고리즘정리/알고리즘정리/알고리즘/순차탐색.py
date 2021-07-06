# 1. 순차 탐색 이란?
# 데이터가 담겨있는 리스트를 앞에서부터 하나씩 비교해서 원하는 데이터를 찾는 방법

def sequencial(data, search):
    for i in range(len(data)):
        if data[i] == search:
            return i
    
    return False

# 2. 시간 복잡도
# O(n)