def reverse(d):
    nd = {}
    for key,value in d.items() : nd[value] = key
    return nd

def keys(d,v):
    l = []
    for key,value in d.items() :
        if value == v : l.append(key)
    return l

exec(input().strip())