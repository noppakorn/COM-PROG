data = {}
N = int(input())
for i in range(N):
    x = [e.strip() for e in input().split(':')]
    data[x[0]] = [e.strip() for e in x[1].split(',')]
out = []
for name,movie in data.items():
    for i in data:
        if i != name :
            for j in data[i] :
                if j in movie: break
            else : out.append([name,i])
if len(sorted(set([tuple(sorted(i)) for i in out]))) == 0: print('None')
else : 
    for i in sorted(set([tuple(sorted(i)) for i in out])): print(i[0],i[1])