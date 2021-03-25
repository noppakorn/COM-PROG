import string
d = {}
for i in input().lower() :
    if i not in string.ascii_lowercase : continue
    if i in d : d[i] += 1
    else : d[i] = 1
l = []
for i in d : l.append([-int(d[i]),i]) 
for i in sorted(l) : print('%s -> %d' % (i[1],-i[0]))