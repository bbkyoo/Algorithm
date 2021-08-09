#def solution(n, k, cmd):
#    arr = []
#    ori = []

#    dump = []
#    for i in range(n):
#        arr.append(str(i))
#        ori.append(str(i))

#    for i in cmd:
#        temp = i.split()
#        if temp[0] == 'D':
#            k += int(temp[1])
#        elif temp[0] == 'U':
#            k -= int(temp[1])
#        elif temp[0] == 'C':
#            dump.append([k, arr.pop(k)])
#            if k == len(arr):
#                k -= 1
#        else:
#            target = arr[k]
#            t = dump.pop()
#            arr.insert(t[0],t[1])
#            k = arr.index(target)

#    result = ''
#    for i in ori:
#        if i in arr:
#            result += 'O'
#        else:
#            result += 'X'

#    return result

def solution(n, k, cmd):
    answer = ''
    
    linked_list = {i: [i-1, i+1] for i in range(1, n+1)}
    OX = ["O" for i in range(1, n+1)]
    stack = []
    
    k += 1
    
    for c in cmd:
        if c[0] == 'D':
            for _ in range(int(c[2:])):
                k = linked_list[k][1]
    
        elif c[0] == 'U':
            for _ in range(int(c[2:])):
                k = linked_list[k][0]
    
        elif c[0] == 'C':
            prev, next = linked_list[k]
            stack.append([prev, next,k])
            OX[k-1] = 'X'

            if next == n+1:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if prev == 0:
                linked_list[next][0] = prev
            elif next == n+1:
                linked_list[prev][1] = next
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev

        elif c[0] == 'Z':
            prev, next, now = stack.pop()
            OX[now-1] = 'O'

            if prev == 0:
                linked_list[next][0] = now
            elif next == n+1:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now

    return "".join(OX)

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]    

print(solution(n, k, cmd))    
    
    
    
    
    

