#r = input().strip()
#target = int(input())
r = 'X2/8/43XXX359/2/6'
target = 0
l = []
i = 0
total_score = 0
for f in range(0,10) :
    if r[f:f+3] == 'XXX' : 
        total_score += 30


###while len(r) > 3 :
###    if r[0] == 'X' : 
###        l.append([r[0]])
###        r.pop(0)
###    else : 
###        l.append(r[0:2])
###        r.pop(0)
###        r.pop(0)
###l.append(r)
###s = [0]*len(l)
###for i in range(len(l)) :
###    for j in l[i] :
###        if i == 'X' : 
###            s[i] += 10
###            
###       elif i == ''