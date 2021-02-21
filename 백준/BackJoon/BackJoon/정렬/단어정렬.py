N = int(input())

word_list = []
for i in range(N):
    word_list.append(input()) 

word_list_result = []
word_list_result = list(set(word_list))

temp = None
for i in range(len(word_list_result)):
    for j in range(i+1,len(word_list_result)):
        if len(word_list_result[i]) > len(word_list_result[j]):
            temp = word_list_result[i]
            word_list_result[i] = word_list_result[j]
            word_list_result[j] = temp

for i in range(len(word_list_result)):
    for j in range(i+1,len(word_list_result)):
        if len(word_list_result[i]) == len(word_list_result[j]):
            if word_list_result[i] > word_list_result[j]:
                temp = word_list_result[i]
                word_list_result[i] = word_list_result[j]
                word_list_result[j] = temp

for i in range(len(word_list_result)):
    print(word_list_result[i])
