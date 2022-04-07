n, s, r = map(int, input().split())
break_nums = list(map(int, input().split()))
have_nums = list(map(int, input().split()))
set_have = set(have_nums) - set(break_nums)
set_lost = set(break_nums) - set(have_nums)

for i in set_have:
    if i-1 in set_lost:
        set_lost.remove(i-1)
    elif i+1 in set_lost:
        set_lost.remove(i+1)

print(len(set_lost))