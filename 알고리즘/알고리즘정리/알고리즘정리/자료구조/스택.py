# 1. 스택구조
# FILO 구조
# 컴퓨터 내부 프로세스 구조의 함수 동작 방식에 사용
# 주요기능 put, pop

# 2. 스택의 장점/단점
# 장점
# 구조가 단순해서, 구현이 쉽다
# 데이터 저장/일기 속도가 빠르다

# 단점
# 데이터 최대 갯수를 미리 정해야 한다
# 저장 공간의 낭비가 발생할 수 있다.

data_stack = list()
data_stack.append(2)
print(data_stack.pop())

# push, pop 직접 구현

stack_list = list()

def push(data):
    stack_list.append(data)

def pop(data):
    data = stack_list[-1]
    del stack_list[-1]
    return data








