from math import gcd

x = str(input()).split(',')
dyn = int(x[0]+x[1]+x[2]) - int(x[0]+x[1])
dyd = (10**(len(x[1])+len(x[2]))) - (10**len(x[1]))
print(dyn//gcd(dyn,dyd),'/',dyd//gcd(dyn,dyd))
