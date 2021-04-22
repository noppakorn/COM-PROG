def add_poly(p1, p2):
    d = {}
    for i,j in p1 :
        if j not in d :d[j] = i
        else : d[j] += i
    for i,j in p2 :
        if j not in d :d[j] = i
        else : d[j] += i
    return [(i[1],i[0]) for i in sorted(list(d.items()))[::-1] if i[1] != 0]

def mult_poly(p1, p2):
    d = {}
    for i,j in p1:
        for k,l in p2:
            if j+l not in d : d[j+l] = i*k
            else : d[j+l] += i*k
    return [(i[1],i[0]) for i in sorted(list(d.items()))[::-1] if i[1] != 0]
            
for i in range(3):
    exec(input().strip())