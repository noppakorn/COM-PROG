d = {}
l = []
for i in open('en_to_th.csv'):
    l.append(i.split('\t')[1:3][::-1])
for k in l:
    d[k[0].strip()] = k[1].strip()
for i in d :
    print(i)
fout = open('TH_COVID_EN.csv','w+')
for i in open('TH_20210401_20210416.csv') :
    ls = i.split(',')
    print(ls[0])
    if ls[0] in d:
        ls[0] = d[ls[0]]
    fout.writelines(','.join(ls))