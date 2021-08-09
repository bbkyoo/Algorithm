import heapq

operations = ["I 16","D 1"]
q = []

for i in operations:
    if i == "D 1" and q:
        q.pop(q.index(max(q)))
    