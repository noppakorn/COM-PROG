import string
d = {}
for i in input().lower() :
    if i not in string.ascii_lowercase : continue
    if i in d.keys() : d[i] += 1
    else : d[i] = 1
l = []
for i in list(d.items()) : l.append([-i[1],i[0]])
for i in sorted(l) : print('%s -> %d' % (i[1],-i[0]))