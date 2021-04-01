gc = int(input())
d = {}
c = 1
sid = input()
while sid != '-':
    d[sid] = c
    c += 1
    sid = input()
    if c > gc : c = 1
ask = input()
while ask != 'quit':
    if ask in d: print(d[ask])
    else: print('not found')
    ask = input()