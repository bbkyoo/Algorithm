def solution(money, limit):
    success = 0
    loss = 0
    count = 0
    isflag = True

    while True:
        if (isflag and money >= limit):
            success += 1
            break
        elif money < limit:
            if limit == 1:
                loss += 1
                break
            limit //= 2
            loss += 1
            if count > 0:
                count -= 1
        elif money >= limit:
            money -= limit
            success += 1
            count += 1
            if count == 2:
                break

        isflag = False

    answer = [success, loss]
    return answer



# def solution(inp_str):
#     answer = []
#     bigAlpha = []
#     smallAlpha = []
#     nums = []
#     specialChar = ['~', '!', '@', '#', '$', '%', '^', '&', '*']
#     notSpecialChar = ['(', ')', '-', '_', '=', '+']
#     bA = False
#     sA = False
#     num = False
#     sC = False
#     numThree = 0
#
#     for i in range(65, 91):
#         bigAlpha.append(chr(i))
#
#     for i in range(97, 123):
#         smallAlpha.append(chr(i))
#
#     for i in range(0, 10):
#         nums.append(str(i))
#
#     if 8 > len(inp_str) or 15 < len(inp_str):
#         answer.append(1)
#
#     for i in inp_str:
#         if (i not in bigAlpha) and (i not in smallAlpha) and (i not in nums) and (i not in specialChar):
#             answer.append(2)
#             break
#
#     for i in inp_str:
#         if i in bigAlpha and bA == False:
#             bA = True
#             numThree += 1
#         elif i in smallAlpha and sA == False:
#             sA = True
#             numThree += 1
#         elif i in nums and num == False:
#             num = True
#             numThree += 1
#         elif i in specialChar and sC == False:
#             sC = True
#             numThree += 1
#
#     if numThree < 3:
#         answer.append(3)
#
#     isFlag = False
#     countSeq = 1
#     if len(inp_str) >= 4:
#         start = inp_str[0]
#         for i in range(1, len(inp_str)):
#             if start == inp_str[i]:
#                 countSeq += 1
#                 if countSeq >= 4:
#                     answer.append(4)
#                     break
#             else:
#                 start = inp_str[i]
#                 countSeq = 1
#
#     for i in inp_str:
#         if inp_str.count(i) >= 5:
#             answer.append(5)
#             break
#
#     if len(answer) == 0:
#         answer.append(0)
#
#     return answer
#
# inp_str = "AaTa+!12-3"
# answer = []
# bigAlpha = []
# smallAlpha = []
# nums = []
# specialChar = ['~','!','@','#','$','%','^','&','*']
# notSpecialChar = ['(',')','-','_','=','+']
# bA = False
# sA = False
# num = False
# sC = False
# numThree = 0
#
# for i in range(65, 91):
#     bigAlpha.append(chr(i))
#
# for i in range(97, 123):
#     smallAlpha.append(chr(i))
#
# for i in range(0, 10):
#     nums.append(str(i))
#
# if 8 > len(inp_str) or 15 < len(inp_str):
#     answer.append(1)
#
# for i in inp_str:
#     if (i not in bigAlpha) and (i not in smallAlpha) and (i not in nums) and (i not in specialChar):
#         answer.append(2)
#         break
#
# for i in inp_str:
#     if i in bigAlpha and bA == False:
#         bA = True
#         numThree += 1
#     elif i in smallAlpha and sA == False:
#         sA = True
#         numThree += 1
#     elif i in nums and num == False:
#         num = True
#         numThree += 1
#     elif i in specialChar and sC == False:
#         sC = True
#         numThree += 1
#
# if numThree < 3:
#     answer.append(3)
#
# isFlag = False
# countSeq = 1
# if len(inp_str) >= 4:
#     start = inp_str[0]
#     for i in range(1,len(inp_str)):
#         if start == inp_str[i]:
#             countSeq += 1
#             if countSeq >= 4:
#                 answer.append(4)
#                 break
#         else:
#             start = inp_str[i]
#             countSeq = 1
#
# for i in inp_str:
#     if inp_str.count(i) >= 5:
#         answer.append(5)
#         break
#
# if len(answer) == 0:
#     answer.append(0)
#
# print(answer)
#
#
#
