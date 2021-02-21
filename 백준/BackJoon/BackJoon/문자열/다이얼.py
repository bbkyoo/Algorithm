st = str(input()).upper()

result = 0

for i in st:
    if (i in ['A','B','C']):
        result += 3
    elif (i in ['D','E','F']):
        result += 4
    elif (i in ['G','H','I']):
        result += 5
    elif (i in ['J','K','L']):
        result += 6
    elif (i in ['M','N','O']):
        result += 7
    elif (i in ['P','Q','R','S']):
        result += 8
    elif (i in ['T','U','V']):
        result += 9
    elif (i in ['W','X','Y','Z']):
        result += 10

print(result)
