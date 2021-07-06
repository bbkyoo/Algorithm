# 1. 해쉬 구조
# 해쉬 테이블: 키(key)에 데이터(value)를 저장하는 데이터 구조
# 파이썬 딕셔너리 타입이 해쉬 테이블의 예
# 파이썬에서는 해쉬를 별도 구현할 이유가 없음 - 딕셔너리가 있기 떄문

# 2. 알아둘 용어
# 해쉬: 임의 값을 고정 길이로 변환한는 것
# 해쉬 테이블: 키 값의 연사에 의해 직접 접근이 가능한 데이터 구조
# 해쉬 함수: Key를 입력으로 받아 산술 연산을 이용해 데이터 위치를 찾는 함수
# 해쉬 값, 해쉬 주소: Key를 해싱 함수로 연산해서, 해쉬 값을 알아내고, 이를 기반으로 해쉬 테이블에서 해당 Key에 대한
# 데이터 위치를 일관성 있게 찾을 수 있음

# 1. 해쉬 테이블 만들기
hash_table = list([0 for i in range(10)])
print(hash_table)

# 2. 해쉬 함수 만들기
def hash_func(key):
    return key % 5

# 3. 해쉬 테이블에 데이터 저장
data1 = "Andy"
data2 = "Dave"
data3 = "Trump"

# 해쉬 함수에 key를 넣어 해쉬 주소가 됨
print(hash_func(ord(data1[0])))

# 3.1 해쉬 테이블에 값 저장

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

storage_data('Andy','01055553333')

# 3.2 실제 데이터를 읽어보기
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data('Andy'))

# 4. 해쉬 테이블의 장단점
# 장점
# 데이터 저장/읽기 속도가 빠르다
# 해쉬는 키에 대한 데이터가 있는 지 확인이 쉬움

# 단점
# 일반적으로 저장공간이 좀더 많이 필요하다
# 여러 키에 해당하는 주소가 동일할 경우 해결하기 위한 별도의 자료구조가 필요하다

# 주요 용도
# 검색이 많이 필요할 경우
# 저장, 삭제, 읽기가 빈번한 경우
# 캐쉬 구현시(중복 확인이 쉽기 떄문)

# 5. 해쉬함수 구현해보기

hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data('Dave','010333322222')
save_data('Andy','010333326666')
print(read_data('Dave'))

# 6. 충돌 해결 알고리즘
# 해쉬 테이블의 가장 큰 문제는 충돌 입니다. 이 것을 해쉬충돌 이라고도 부릅니다.

# 6.1 Chaining 기법
# 개방 해시 또는 오픈 해싱 기법 중 하나 입니다.
# 링크드 리스트를 사용해서 데이터를 뒤에 추가로 저장시켜 해결하는 방법
 
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key,value])
    else:
        hash_table[hash_address] = [[index_key,value]]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None

print(hash("Dave") % 8)
print(hash("Dd") % 8)
print(hash("Data") % 8)

save_data("Dd","12344321")
save_data("David","56788765")
print(read_data("Dd"))

# 6.2 Linear Probing 기법
# 패쇄 해싱 또는 Closing Hasing 기법 중 하나

hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]
        
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address,len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None

print(hash('dk')%8)
print(hash('da')%8)

save_data('dk','01236621')
save_data('da','43215235')
print(read_data('dk'))

# 6.3 빈번한 충돌을 개선하는 방법
# 그러면 공간을 2배로 늘린다.
# 예) hash_table = [0 for _ in range(16)]

# 7.시간복잡도
# 일반적인 경우(충돌이 없는 경우)는 O(1)
# 최악의 경우(모두의 해시 주소가 같은 경우) O(n)

# 검색해서 해쉬 테이블의 사용 예
# - 16개의 배열에 데이터를 저장하고, 검색할 때 O(n)
# - 16개의 데이터 저장공간을 가진 위의 해쉬 테이블에 데이터를 저장하고, 검색할 때 O(1)













