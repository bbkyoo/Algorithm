import sys

n = int(sys.stdin.readline())

lt = []
for _ in range(n):
    x = sys.stdin.readline() 
    if 'push' in x:
        lt.append(int(x.split()[1]))
    elif 'pop' in x:
        if len(lt) == 0:
            print(-1)
        else:
            print(lt[-1])
            lt.pop()
    elif 'size' in x:
        print(len(lt))
    elif 'empty' in x:
        if len(lt) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in x:
        if len(lt) == 0:
            print(-1)
        else:
            print(lt[-1])
