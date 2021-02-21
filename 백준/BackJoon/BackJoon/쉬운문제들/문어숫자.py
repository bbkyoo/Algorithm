while True:
    N = input()
    result = 0
    num = 0
    
    if N == '#':
        break
    for i in range(len(N)):
        if N[i] == '-':
            num = 0
            result = result + num*(8**(len(N)-1-i))
        elif N[i] == '\\':
            num = 1
            result = result + num*(8**(len(N)-1-i))
        elif N[i] == '(':
            num = 2
            result = result + num*(8**(len(N)-1-i))
        elif N[i] == '@':
            num = 3
            result = result + num*(8**(len(N)-1-i))
        elif N[i] == '?':
            num = 4
            result = result + num*(8**(len(N)-1-i))
        elif N[i] == '>':
            num = 5
            result = result + num*(8**(len(N)-1-i))
        elif N[i] == '&':
            num = 6
            result = result + num*(8**(len(N)-1-i))
        elif N[i] == '%':
            num = 7
            result = result + num*(8**(len(N)-1-i))
        elif N[i] == '/':
            num = -1
            result = result + num*(8**(len(N)-1-i))   
    print(result)













