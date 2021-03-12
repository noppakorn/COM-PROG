x = [e for e in input().split()]
fin = open(x[0])
l = []
for i in fin.readlines() :
    i = i.split()
    if i[0][:2] == x[1][-2:] : l.append(float(i[1]))
if len(l) == 0 : print('No data')
else : print(min(l),max(l),sum(l)/len(l))