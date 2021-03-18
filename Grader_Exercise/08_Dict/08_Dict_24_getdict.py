import string
l = []
for i in range(2,10) :
    i = str(i)
    if i == '7' or i == '9' : l += [i,i*2,i*3,i*4]
    else : l += [i,i*2,i*3]
k2t,t2k = {},{}
for i,j in zip(l,string.ascii_lowercase):
    k2t[i] = j
    t2k[j] = i

print(t2k)
print(k2t)