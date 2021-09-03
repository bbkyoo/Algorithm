# 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

mouem = ['a','e','i','o','u']
zauem = []

for i in range(97, 123):
    if chr(i) not in mouem:
        zauem.append(chr(i))

while True:
    s = input()
    result = s
    if s == "end":
        break

    s = list(s)

    isTrue = False
    
    for i in range(len(s)):
        if s[i] in mouem: # 1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
            isTrue = True

        if len(s) >= 3: # 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
            if 0 <= i < len(s) and 0 <= i+1 < len(s) and 0 <= i+2 < len(s):
                if s[i] in mouem and s[i+1] in mouem and s[i+2] in mouem:
                    isTrue = False
                    break
                elif s[i] in zauem and s[i+1] in zauem and s[i+2] in zauem:
                    isTrue = False
                    break

        if len(s) >= 2: # 3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
            if 0 <= i < len(s) and 0 <= i+1 < len(s):
                if s[i] != 'e' and s[i] != 'o':
                    if s[i] == s[i+1]:
                        isTrue = False
                        break

    if isTrue:
        print("<{}> is acceptable.".format(result))
    else:
        print("<{}> is not acceptable.".format(result))
    





