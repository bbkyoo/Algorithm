while True:
    sentence = input()
    
    if sentence == '#':
        break
    
    s = sentence.lower()
    count = 0
   
    print(s[0], s.count(s[0]) - 1)