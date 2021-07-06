# 1. 힙 이란
# 힙: 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리
# 힙을 사용하는 이유
# - 배열에 데이터를 넣고, 최대값과 최소값을 찾으려면 O(n)이 걸림
# - 이에 반해, 힙에 데이터를 넣고, 최대값과 최소값을 찾으면 O(log(n))이 걸림
# - 우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료구조 및 알고리즘 구현 등에 활용됨

# 2. 힙 구조
# 최대값을 구하기 위한 최대 힙, 최소값을 구하기 위한 최소 힙
# 힙은 다음과 같이 두 가지 조건을 갖고 있다.
# - 각 노드의 값은 해당 노드의 자식 노드가 가진 값 보다 크다(최대 힙)
# - 각 노드의 값은 해당 노드의 자식 노드가 가진 값 보다 작다(최소 힙)
# - 완전 이진 트리의 형태를 갖음

# 3. 힙과 이진 탐색 트리의 공통점과 차이점
# 공통점: 힙과 이진 탐색 트리는 모두 이진 트리임
# 차이점
# - 힙은 각 노드의 값이 자식 노드보다 크거나 같음(최대 힙의 경우)
# - 이진 탐색 트리는 왼쪽자식이 값이 가장 작고, 그 다음 부모 노드, 그 다음 오른쪽 자식 노드 값이 가장 큼
# - 힙은 이진 탐색 트리의 조건인 자식 노드에서 작은 값은 왼쪽, 큰 값은 오른쪽이라는 조건은 없음
# - 이진 탐색 트리는 탐색을 위한 구조, 힙은 최대/최소값 겁색을 위한 구조 중 하나로 이해하면 됨 

# 4. 힙 삽입 과정(최대 힙의 예)
# 힙은 부모 노드를 중심으로 왼쪽부터 채워짐(삽입과정)
# 삽입할 데이터가 힙의 데이터보다 클 경우(최대 힙의 경우)
# 부모 노드와 위치를 바꾸어주는 작업을 반복함

# 5. 힙 삭제 과정(최대 힙의 예)
# 보통 root 노드를 삭제한다.
# 가장 마지막에 삽입되었던 노드를 root 노드로 올린다
# root 노드를 기준으로 자식노드와 비교해서 더 큰값을 root 노드와 바꾼다

# 6. 힙 구현

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)

        inserted_idx = len(self.heap_array)-1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx],self.heap_array[parent_idx] = self.heap_array[parent_idx],self.heap_array[inserted_idx] 
            inserted_idx = parent_idx

        return True

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        # case1: 왼쪽 자식 노드도 없을 때  
        if left_child_popped_idx >= len(self.heap_array):
            return False

        # case2: 오른쪽 자식 노드만 없을때
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False

        # case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
        else:
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap_array) <= 1: # 데이터가 없을 때
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]

        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # case2: 오른쪽 자식 노드만 없을때
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]  
                    popped_idx = left_child_popped_idx

            # case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]  
                        popped_idx = left_child_popped_idx
                else:
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]  
                        popped_idx = right_child_popped_idx

        return returned_data

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)


# 7. 힙의 시간복잡도
# depth를 h라고 보면
# n개의 노드를 가지는 heap에 데이터 삽입 또는 삭제시, 최악의 경우 root 노드에서 leaf노드까지 비교해야 하므로
# h = log(n)에 가까우므로, 시간복잡도는 O(log(n))
# 한번 실행마다, 50%의 실행할 수 도 있는 명령을 제거한다는 의미, 즉 50%의 실행시간을 단축시킬 수 있다는 것을 의미




























