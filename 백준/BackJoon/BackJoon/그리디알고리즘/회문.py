def pseudo(sentence, left, right):
    while left < right:
        if sentence[left] == sentence[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def palindrome(sentence, left, right):
    while left < right:
        if sentence[left] == sentence[right]:
            left += 1
            right -= 1
        else:
            result1 = pseudo(sentence, left+1, right)
            result2 = pseudo(sentence, left, right-1)
            if result1 == True or result2 == True:
                return 1
            else:
                return 2
    return 0      

T = int(input())

for _ in range(T):
    sentence = list(input())
    result = palindrome(sentence , 0 , len(sentence)-1)
    print(result)
