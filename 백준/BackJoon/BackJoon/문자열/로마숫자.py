nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
extra = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

def to_num(s):
    res = 0
    n = len(s)
    idx = 0

    while idx < n:
        if idx == n-1:
            res += nums[s[idx]]
            break

        flag = True

        if s[idx] == 'I':
            if s[idx+1] == 'V' or s[idx+1] == 'X':
                res += extra[s[idx:idx+2]]
                flag = False

        elif s[idx] == 'X':
            if s[idx+1] == 'L' or s[idx+1] == 'C':
                res += extra[s[idx:idx+2]]
                flag = False

        elif s[idx] == 'C':
            if s[idx+1] == 'D' or s[idx+1] == 'M':
                res += extra[s[idx:idx+2]]
                flag = False

        if not flag:
            idx += 2
        else:
            res += nums[s[idx]]
            idx += 1

    return res

first = input()
second = input()
total = to_num(first) + to_num(second)
print(total)

ans = ''
total = str(total)
t = len(total)
n = len(total)

while n:
    num = int(total[t-n])
    if n == 4:
        ans += 'M'*num

    elif n == 3:
        if num == 9:
            ans += 'CM'
        elif num == 4:
            ans += 'CD'
        else:
            if num >= 5:
                ans += 'D'
            ans += 'C'*(num%5)

    elif n == 2:
        if num == 9:
            ans += 'XC'
        elif num == 4:
            ans += 'XL'
        else:
            if num >= 5:
                ans += 'L'
            ans += 'X'*(num%5)

    elif n == 1:
        if num == 9:
            ans += 'IX'
        elif num == 4:
            ans += 'IV'
        else:
            if num >= 5:
                ans += 'V'
            ans += 'I'*(num%5)

    n -= 1

print(ans)











































