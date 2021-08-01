color = ["RG", "WR","BW", "GG"]
prices = [2000, 6000]

dic1 = {}
dic2 = {}

for i in color:
    if i[0] not in dic1:
        dic1[i[0]] = 1
    else:
        dic1[i[0]] += 1

    if i[1] not in dic2:
        dic2[i[1]] = 1
    else:
        dic2[i[1]] += 1

method1 = 0

for i, v in dic1.items():
    if i in dic2:
        temp = min(dic1[i], dic2[i])
        method1 += temp
        dic1[i] -= temp
        dic2[i] -= temp

method2 = min(sum(dic1.values()),sum(dic2.values())) * 2
print(method2)
#result1 = (method1 * prices[0])
#result2 = (method2 // 2 )* prices[1]

#answer1 = result1 + result2
#answer2 = result1 + method2*prices[0]
#print(result1)
#print(answer2)



