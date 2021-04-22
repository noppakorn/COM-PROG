d = {}
for i in range(int(input())):
    ii = input().split()
    d[ii[0]] = ii[1:]
out = []
ii = set(input().split())
for i in d: 
    if ii.issubset(d[i]) : out.append([i,d[i]])
if len(out) == 0 :
    print('Not Found')
else :
    for i in sorted(out): print(i[0],i[1][0],i[1][1],i[1][2])