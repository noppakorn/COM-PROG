d = {}
for i in range(int(input())) :
    x = input().split()
    d[x[0]] = int(x[1])
cd = {}
for i in range(int(input())):
    x = input().split()
    if x[0] in d :
        if x[0] in cd : cd[x[0]] += int(x[1])*d[x[0]]
        else : cd[x[0]] = int(x[1])*d[x[0]]
if len(cd) == 0 : print('No ice cream sales')
else : 
    su = 0
    for i in cd : su += cd[i]
    print('Total ice cream sales: %.1f' % su)
    top = []
    ma = 0
    for key in cd :
        if cd[key] > ma : ma = cd[key]
    for key in cd :
        if cd[key] == ma : top.append(key)
    print('Top sales: %s ' % ', '.join(sorted(top)))