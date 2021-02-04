l = str(input()).split(' ')
fl = [float(l[0]),float(l[1]),float(l[2]),float(l[3])]

min = fl[0]
if fl[1] <= min : min = fl[1]
if fl[2] <= min : min = fl[2]
if fl[3] <= min : min = fl[3]

max = fl[0]
if fl[1] >= max : max = fl[1]
if fl[2] >= max : max = fl[2]
if fl[3] >= max : max = fl[3]

print(round((fl[0]+fl[1]+fl[2]+fl[3]-max-min)/2,2))