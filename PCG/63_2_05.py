x = [e for e in input().split()]
g = ['F','D','C','B','A']
s,c = 0,0
for i in x :
    if i in g :
        s += float(g.index(i))
        c += 1
    else :
        c += 1
print(round(s/c,2))