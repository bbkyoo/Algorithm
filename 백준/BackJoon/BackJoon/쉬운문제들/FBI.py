sentence = [input() for i in range(5)]
index = []
for i in range(5):
    if 'FBI' in sentence[i]:
        index.append(i+1)
    else:
        continue

if index:
    for i in range(len(index)):
        print(index[i], end=" ")
else:
    print("HE GOT AWAY!")