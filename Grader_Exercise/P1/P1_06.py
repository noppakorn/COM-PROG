op = input()
r = int(input())
l = [input() for i in range(r)]
for i in l :
    if len(i) != len(l[0]) : 
        print('Invalid size')
        exit(0)
if op == '90' :
    s = ''.join(l)
    for i in range(0,len(l[0])) :
        for j in range(-len(l[0])+i,(-len(l[0])*r)-1,-len(l[0])) : 
            if abs(j) == (len(l[0])*r)-i : print(s[j])
            else : print(s[j],end='')
elif op == '180' :
    for i in range(-1,-len(l)-1,-1) : print(l[i][::-1])
elif op == 'flip' :
    for i in l : print(i[::-1])