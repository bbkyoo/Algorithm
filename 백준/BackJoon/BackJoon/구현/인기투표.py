t = int(input())

for _ in range(t):
    n = int(input())

    ticket = []
    for _ in range(n):
        ticket.append(int(input()))

    mx = max(ticket) 
    cnt = ticket.count(mx)
    
    if cnt >= 2:
        print("no winner")
    else: 
        sm = sum(ticket)
        if mx > sm // 2:
            print("majority winner {}".format(ticket.index(mx) + 1))
        else:
            print("minority winner {}".format(ticket.index(mx) + 1))

