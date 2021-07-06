# 1. 큐 구조
# FIFO 구조

# 2. 알아둘 용어
# Enqueue: 큐에 데이터를 넣는 기능
# Dequeue: 큐에 데이터를 꺼내는 기능

import queue

data_queue = queue.Queue()
data_queue.put("배")
data_queue.put("병규")
print(data_queue.qsize())
print(data_queue.get()) # 맨 먼저 들어간 데이터 출력하면서 꺼냄
print(data_queue.qsize())

# 3. LifoQueue 마지막에 넣은 것이 먼저 추출

data_lifoqueue = queue.LifoQueue()

data_lifoqueue.put("문")
data_lifoqueue.put("지수")
print(data_lifoqueue.qsize())
print(data_lifoqueue.get())
print(data_lifoqueue.qsize())

# 4. 우선순위 큐 -> 우선순위도 지정해야 함(값이 작은 것이 우선순위가 높은 것)
data_PriorityQueue = queue.PriorityQueue()
data_PriorityQueue.put((10,"김"))
data_PriorityQueue.put((9,"연수"))

print(data_PriorityQueue.qsize())
print(data_PriorityQueue.get())
print(data_PriorityQueue.qsize())

# 어디에 큐가 많이 쓰일까?
# 멀티테스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해서 많이 사용됨

# enqueue, dequeue 구현
queue_list = list()
def enqueue(data):
    queue_list.append(data)

def dequeue(data):
    data = queue_list[0]
    del queue_list[0]
    return data











