N = int(input())

# find로 인덱스 비교로 찾는 문제 

for _ in range(N):
    sentence = input()
    for j in range(1,len(sentence)):
        if sentence.find(sentence[j-1]) > sentence.find(sentence[j]):
            N -= 1
            break
print(N)