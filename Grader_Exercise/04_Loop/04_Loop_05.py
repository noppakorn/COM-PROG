match = input()
x = input()
c = 0
l = []
for i in x :
    if i not in '"(),.' and i not in ("'") : l.append(i)
    else : l.append(' ')
for i in ''.join(l).split(' ') : 
    if i == match : c += 1
print(c)