N = int(input())

login_list = []

for _ in range(N):
    age, name = map(str,input().split())    
    login_list.append([int(age), name])

login_list.sort(key=lambda x : x[0])

for i in range(N):
    print(login_list[i][0],login_list[i][1])


            