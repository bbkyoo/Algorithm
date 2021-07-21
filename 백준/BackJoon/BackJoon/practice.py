n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
pos = [0]*(n+1)

for i in range(n):
    pos[inorder[i]] = i

def pre_order(in_start, in_end, post_start, post_end):
    if post_start <= post_end:
        parents = postorder[post_end]

        print(parents, end=' ')
        p_index = pos[parents]
        start_count = p_index - in_start
        end_count = in_end - p_index

        pre_order(in_start, in_start + start_count - 1, post_start, post_start+start_count-1)
        pre_order(in_end - end_count + 1, in_end, post_end - end_count, post_end - 1)
