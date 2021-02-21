num1, num2 = input().split()

revers_num1 = int(num1[::-1])
revers_num2 = int(num2[::-1])

if(revers_num1 > revers_num2):
    print(revers_num1)
else:
    print(revers_num2)


