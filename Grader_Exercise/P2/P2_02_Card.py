x = input()
d = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'C':1,'D':2,'H':3,'S':4}
l = []
for i in range(len(x)//2-1):
    if d[x[2*i]] == d[x[2*i+2]]: l.append(d[x[2*i+1]]-d[x[2*i+3]])
    else: l.append(d[x[2*i]] - d[x[2*i+2]])
for i in l:
    if i>0: print('+%d' % i,end='')
    else: print(i,end='')