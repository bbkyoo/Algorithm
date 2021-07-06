import random

# 1. 트리 구조
# 트리: Node(정점)와 Branch(간선)를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조
# 실제 어디에 많이 사용되나?
# 트리 중 이진 트리 형태 구조로 탐색 알고리즘 구현을 위해 많이 사용됨 

# 2. 알아둘 용어
# Node: 트리에서 데이터를 저장하는 기본 요소
# Level: 최상위 노드를 Level0으로 하였을 때, 하위 Branch로 연결된 노드의 깊이를 나타냄
# Parent Node: 어떤 노드의 다음 레벨에 연결된 노드
# Child Node: 어떤 노드의 상위 레벨에 연결된 노드
# Leaf Node: Child Node가 하나도 없는 노드
# Sibling(형제): 동일한 Parent Node를 가진 노드

# 3. 이진 트리와 이진 탐색 트리(Binary Search Tree)
# 이진 트리: 정점의 최대 간선이 2인 트리
# 이진 탐색 트리: 이진 트리에 다음과 같은 조건이 추가된 노드
# - 왼쪽 노드는 키 노드보다 작은 값, 오른쪽 노드는 키 노드보다 큰 값

# 4. 자료 구조 이진 탐색 트리의 장점과 주요 용도
# 주요 용도: 데이터 검색(탐색)
# 장점: 탐색 속도를 개선할 수 있음

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
class NodeMgnt:
    def __init__(self, head):
        self.head = head
    
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    # 5. 이진 탐색 트리 탐색
    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right

        return False

head = Node(1)
BST = NodeMgnt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)

print(BST.search(4))

# Case 5.1 Leaf_Node 삭제
# Case 5.2 자식이 하나인 Node 삭제
# Case 5.3 자식이 두개인 Node 삭제

# 1. 삭제할 노드의 오른쪽 자식중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키게 할 경우
# (면접에서는 안 물어봄)
# 삭제할 Node의 오른쪽 자식 선택
# 해당 Node를 삭제할 Node의 Parent Node의 왼쪽 Branch가 가리키게 함
# 해당 Node의 왼쪽 Branch가 삭제랑 Node의 왼쪽 Child Node를 가리키게 함
# 해당 Node의 오른쪽 Branch가 삭제할 Node의 오른쪽 Child Node를 가리키게 함
# 만약 해당 node가 오른쪽 Child를 가지고 있었을 경우에는, 해당 Node의 본래
# Parent Node의 왼쪽 Branch가 해당 Child_Node를 가리키게 함 

# 삭제 코드
def delete(self, value):
    searched = False
    self.current_node = self.head
    self.parent = self.head
    while self.current_node:
        if self.current_node.value == value:
            searched = True
            break
        elif value < self.current_node:
            self.parent = self.current_node
            self.current_node = self.current_node.left
        else:
            self.parent = self.current_node
            self.current_node = self.current_node.right

    if searched == False:
        return False

    # 이후부터 Case들을 분리해서, 코드 작성
    # Case1 삭제할 노드가 Leaf Node인 경우

    # self.current_node가 삭제할 Node, self.parent는 삭제할 Node의 Parent Node인 상태
    if self.current_node.left == None and self.current_node.right == None:
        if value < self.parent.value:
            self.parent.left = None
        else:
            self.parent.right = None
        del self.current_node

    # Case2 삭제할 노드가 Child Node를 한 개 가지고 있을 경우
    # 왼쪽일때
    if self.current_node.left and self.current_node.right == None:
        if value < self.parent.value:
            self.parent.left = self.current_node.left
        else:
            self.parent.right = self.current_node.left
    
    # 오른쪽 일때
    elif self.current_node.left == None and self.current_node.right:
        if value < self.parent.value:
            self.parent.left = self.current_node.right
        else:
            self.parent.right = self.current_node.right

    # 삭제할 Node가 Child Node를 두개 가지고 있을 경우
    # 1-1 삭제할 노드가 Parent Node의 왼쪽에 있을 경우
        # 1-1-1 삭제할 Node의 오른쪽 자식중 가장 작은 값을 가진 Node의 Child Node가 없을 때
            
        # 1-1-2 삭제할 Node의 오른쪽 자식중 가장 작은 값을 가진 Node의 오른쪽에 Child Node가 있을 때

    if self.current_node.left and self.current_node.right:
        if value < self.parent.value: # 1-1
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right
            while self.change_node.left:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            
            self.change_node_parent.left = None
            if self.change_node.right: # 1-1-2
                self.change_node_parent.left = self.change_node.right
            else: # 1-1-1
                self.change_node_parent.left = None

            self.parent.left = self.change_node
            self.change_node.right = self.current_node.right
            self.change_node.left = self.change_node.left

    # 1-2 삭제할 노드가 Parent Node의 오른쪽에 있을 경우
        # 1-2-1 삭제할 Node의 오른쪽 자식중 가장 작은 값을 가진 Node의 Child Node가 없을 때
            
        # 1-2-2 삭제할 Node의 오른쪽 자식중 가장 작은 값을 가진 Node의 오른쪽에 Child Node가 있을 때

    else:
        self.change_node = self.current
        self.change_node_parent = self.current_node.right
        while self.change_node.left:
            self.change_node_parent = self.change_node
            self.change_node = self.change_node.left
        if self.change_node.right:
            self.change_node_parent.left = self.change_node.right
        else:
            self.change_node_parent.left = None
        self.parent.right = self.change_node
        self.change_node.left = self.current_node.left
        self.change_node.right = self.current_node.right
   
# 테스트 코드, 1-1000 숫자 중에서 임의로(random) 100개를 추출해서, 이진 탐색 트리에 입력, 검색, 삭제        

# 1-1000 중, 100 개의 숫자 랜덤 선택
bst_nums = set()
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))

# 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
head = Node(500)
binary_tree = NodeMgnt(head)
for num in bst_nums:
    binary_tree.insert(num)

# 입력한 100개의 숫자 검색(검색 기능 확인)
for num in bst_nums:
    if binary_tree.search(num) == False:
        print("search faild", num)
        break

# 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0,99)])

# 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete failed', del_num)

# 6. 이진 탐색 트리의 시간 복잡도와 단점
# depth(트리의 높이)를 h라고 표현 한다면 O(h)
# n개의 노드를 가진다면, h = log(n)에 가까우므로, 시간 복잡도는 O(log(n)) 

# 단점
# 평균 시간 복잡도는 O(log(n))이지만
# 최악의 경우는 링크드리스트와 동일한 성능을 보여줌(O(n))













