import math
l = []
for i in range(int(input())) : l.append([float(e) for e in input().split()])
for i in range(len(l)) : l[i] = [math.sqrt(l[i][0]**2+l[i][1]**2),l[i][0],l[i][1]]
third = sorted(l)[2]
print('#'+str(l.index(third)+1)+': '+'('+', '.join([str(e) for e in third[1:]])+')')