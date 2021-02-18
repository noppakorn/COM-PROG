l = []
a = input()
for i in range(10) :
    if str(i) not in a : l.append(str(i))
if l != [] :
    for i in range(len(l)) :
        if i < len(l)-1 : print(l[i]+',',end='')
        else : print(l[i])
else : print('None')