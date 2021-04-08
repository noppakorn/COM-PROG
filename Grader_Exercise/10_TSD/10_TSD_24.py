inp = [e.strip() for e in input().split(',')]
d = {}
order = []
while inp != ['q']:
    if inp[1] not in d : 
        order.append(inp[1])
        d[inp[1]] = inp[0],
    else : d[inp[1]] += inp[0],
    inp = [e.strip() for e in input().split(',')]
for i in order:
    print(i,end=': ')
    for k in d[i][:-1]: 
        print(k,end=', ')
    print(d[i][-1])