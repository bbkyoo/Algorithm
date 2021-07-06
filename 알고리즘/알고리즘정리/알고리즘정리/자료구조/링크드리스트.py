# 1. 링크드리스트의 구조
# 배열은 연결된 공간에 데이터를 나열하는 데이터 구조
# 링크드리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
# 장점
# 미리 데이터 공간을 할당하지 않아도 됨
# 단점
# 연결을 위한 별도 데이터 공간이 필요하므로, 저장공간 효율이 높지 않음
# 연결 정보를 찾는 시간이 필요하므로 접근 속도가 느림
# 중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성하는 부가적인 작업일 필요

# 기본 링크드리스트 외우기

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgnt:
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self): # 데이터 순회하여 출력하는 함수
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다.")
            return

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next.data
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next

linkedlist1 = NodeMgnt(0)

for data in range(1, 10):
    linkedlist1.add(data)

linkedlist1.delete(1)
linkedlist1.desc()



print("-----------------------")

# 이중 링크드 리스트

class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgnt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self, data):
        if self.head == None:
            return False

        node = self.head

        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self, data):
        if self.head == None:
            return False

        node = self.tail

        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def insert_before(self, data, before_data): # data 중간 삽입
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new
            return True



double_linked_list = NodeMgnt(0)

for data in range(1, 10):
    double_linked_list.insert(data)
double_linked_list.desc()

print('------------------------------------------------')

node_3 = double_linked_list.search_from_tail(3)
if node_3:
    print(node_3.data)
else:
    print('NULL')

double_linked_list.insert_before(2,1.5)
double_linked_list.desc()






















