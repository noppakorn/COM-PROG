B = {1,2,3}
A = {2}
d1 = {1:2,3:2}
d2 = dict( [ (v, k) for (k, v) in d1.items()] )
print(d2)