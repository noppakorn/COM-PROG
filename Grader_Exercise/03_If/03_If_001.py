a,b,c,d,e = int(input()),int(input()),int(input()),int(input()),int(input())
if a > b : a,b = b,a
if c > d : c,d = d,c
if a > c :
    b,d = d,b
    c = a
a = e
if a > b : a,b = b,a
if c > a : 
    b,d = d,b
    a = c
if a > d : print(d)
else : print(a)