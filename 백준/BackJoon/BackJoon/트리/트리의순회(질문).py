# 후위순회에서 마지막은 루트이다
# 중위순회는 루트를 기준으로 왼쪽과 오른쪽으로 나눈다.
# 트리를 구하고 다시 전위순회를 구하는 방식으로 구현    
# https://whereisend.tistory.com/112 참고

import sys
sys.setrecursionlimit(10**9)

N = int(input())

inorder = list(map(int, input().split())) # 중위 순회
postorder = list(map(int, input().split())) # 후위 순회
pos = [0]*(N+1) # 인자를 찾을 때 한번에 찾기 위해

for i in range(N):
    pos[inorder[i]] = i

def pre_order(in_start, in_end, post_start, post_end): # 중위순회 범위, 후위순회 범위
    if post_start <= post_end:
        parents = postorder[post_end] # 후위순회에서 부모노드 찾기
        
        print(parents, end=" ")
        p_index = pos[parents]
        start_count = p_index - in_start # 왼쪽 인자 갯수
        end_count = in_end - p_index # 오른쪽 인자 갯수

        pre_order(in_start, in_start + start_count - 1, post_start, post_start + start_count - 1) # 부모 노드 기준 왼쪽 노드 
        pre_order(in_end - end_count + 1 , in_end , post_end - end_count , post_end - 1) # 부모 노드 기준 오른쪽 노드
        
pre_order(0, N-1, 0, N-1)




