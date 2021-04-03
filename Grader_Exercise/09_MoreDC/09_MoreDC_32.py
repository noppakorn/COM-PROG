def first_fit(L,e):
    stat = 0
    for i in L:
        if sum(i)+e <= 100: 
            i.append(e)
            stat += 1
            break
    if not stat: L.append([e]) 

def best_fit(L,e):
    stat = 0
    suml = [sum(i)+e if sum(i)+e <= 100 else False for i in L]
    if len(suml) != 0 and max(suml) != 0 : L[suml.index(max(suml))].append(e)
    else: L.append([e])

def partition_FF(D):
    l = [[D[0]]]
    for i in D[1:]: first_fit(l,i)
    return l

def partition_BF(D):
    l = [[D[0]]]
    for i in D[1:]: best_fit(l,i)
    return l

exec(input().strip())