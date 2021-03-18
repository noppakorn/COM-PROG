d = {}
for i in range(int(input())) :
    x = input().split()
    d[x[0]] = int(x[1])
cd = {}
for i in range(int(input())):
    x = input().split()
    if x[0] in d.keys() :
        if x[0] in cd.keys() : cd[x[0]] += int(x[1])*d[x[0]]
        else : cd[x[0]] = int(x[1])*d[x[0]]
if len(cd) == 0 : print('No ice cream sales')
else : 
    print('Total ice cream sales: %.1f' % sum(cd.values()))
    top = []
    for key,values in cd.items() :
        if values == max(cd.values()) : top.append(key)
    print('Top sales: %s ' % ', '.join(sorted(top)))