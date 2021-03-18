def reverse(d):
    nd = {}
    for key,value in d.items() : nd[value] = key
    return nd

d = {}
for i in range(int(input())) :
    x = input().split()
    d[x[0]+' '+x[1]] = x[2]
rd = reverse(d)
for i in range(int(input())) :
    y = input()
    if y in d.keys() : print('%s --> %s' % (y,d[y]))
    elif y in rd.keys() : print('%s --> %s' % (y,rd[y]))
    else : print('%s --> %s' % (y,'Not found'))