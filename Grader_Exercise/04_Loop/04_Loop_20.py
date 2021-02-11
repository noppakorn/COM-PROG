l = []
while True :
    z = input()
    if z == 'Zig-Zag' or z == 'Zag-Zig' : break 
    else : l += [int(i) for i in z.split(' ')]

if z == 'Zig-Zag' : 
    mn = l[0]
    mx = l[1]
    for i in range(0,len(l),4) :
        if l[i] < mn : mn = l[i]
    for i in range(3,len(l),4) :
        if l[i] < mn : mn = l[i]
    for i in range(1,len(l),4) :
        if l[i] > mx : mx = l[i]
    for i in range(2,len(l),4) :
        if l[i] > mx : mx = l[i]

elif z == 'Zag-Zig' : 
    mn = l[1]
    mx = l[0]
    for i in range(0,len(l),4) :
        if l[i] > mx : mx = l[i]
    for i in range(3,len(l),4) :
        if l[i] > mx : mx = l[i]
    for i in range(1,len(l),4) :
        if l[i] < mn : mn = l[i]
    for i in range(2,len(l),4) :
        if l[i] < mn : mn = l[i]

print(mn,mx)