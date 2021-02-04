import math
mu = float(input())
sig = float(input())
x = float(input())

f = (1/(sig*math.sqrt(2*math.pi)))*math.exp(-((x-mu)**2)/(2*sig**2))
print(round(f,8))