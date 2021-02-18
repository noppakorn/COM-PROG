x = [int(e) for e in input().split()]
x.sort()
ph = float('nan')
l = []
for i in range(len(x)) :
    if x[i] != ph : 
        ph = x[i]
        l.append(x[i])
c = len(l)
print(c)
if c <=10 : print(l)
else : print(l[:10])