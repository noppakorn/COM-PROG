x = [float(e) for e in input().split()]
l = [0]*(2*len(x)-1)
l[::2] = x
for i in range(1,len(l),2) : l[i] = (l[i-1]+l[i+1])/2
print(l)