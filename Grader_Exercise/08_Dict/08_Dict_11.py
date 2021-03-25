def reverse(d):
    nd = {}
    for key in d : nd[d[key]] = key
    return nd

def keys(d,v):
    l = []
    for key in d:
        if d[key] == v : l.append(key)
    return l

exec(input().strip())