def solution(new_id):
    new_id = new_id.lower()
    n_id = ""
    for i in range(len(new_id)):
        if new_id[i] in ['-','_','.'] or new_id[i].isalpha() or new_id[i].isdigit():
            n_id += new_id[i]

    temp = ''
    if len(n_id) >= 2: 
        for i in range(1, len(n_id)):
            if n_id[i-1] == '.':
                if n_id[i] == '.':
                    continue
                else:    
                    temp += n_id[i-1]
            else:
                temp += n_id[i-1]

        temp += n_id[-1]
    else:
        temp = n_id

    temp = list(temp)
    while True:
        if (len(temp) == 0) or (temp[-1] != '.' and temp[0] != '.'):
            break
        if temp and temp[0] == '.':
            temp.pop(0)
        if temp and temp[-1] == '.':
            temp.pop()

    if len(temp) == 0:
        temp.append('a')

    if len(temp) >= 16:
        temp = temp[:15]

    if temp[-1] == '.':
        temp.pop()

    if len(temp) <= 2:
        while len(temp) < 3:
            temp.append(temp[-1])

    return ''.join(temp)








