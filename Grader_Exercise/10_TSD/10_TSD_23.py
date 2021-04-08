d = {}
for i in range(int(input())):
    x = [e.strip() for e in input().split(',')]
    minu,sec = [int(e) for e in x[3].split(':')]
    if x[2] not in d: d[x[2]] = minu*60+sec
    else : d[x[2]] += minu*60+sec
d = {-j:i for i,j in d.items()}
for i,j in sorted(d.items())[:min(3,len(d))] : print('%s --> %d:%02d' % (j,-i//60,-i%60))