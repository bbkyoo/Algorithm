S = list(input())
k = input()

num_list = ['0','1','2','3','4','5','6','7','8','9']

result = 0

for i in range(len(num_list)):
    if num_list[i] in S:
        S.remove(num_list[i])

S_result = S[0]
for i in range(1,len(S)):
    S_result += S[i]

if k in S_result:
    print(1)
else:
    print(0)