d = {
 0 : 'soon',
 1 : 'neung',
 2 : 'song',
 3 : 'sam',
 4 : 'si',
 5 : 'ha',
 6 : 'hok',
 7 : 'chet',
 8 : 'paet',
 9 : 'kao',
 10 : 'sip',
 100 : 'roi',
 1000 : 'pun',
}

def to_Thai(N):
    if N == 0: return 'soon'
    l = []
    tho = N // 1000 % 10
    hun = N // 100 % 10
    ten = N // 10 % 10
    dec = N  % 10
    if tho>0:
        l.append(d[tho])
        l.append(d[1000])
    if hun>0:
        l.append(d[hun])
        l.append(d[100])
    if ten>0:
        if ten == 1 :
            l.append(d[10])
        if ten == 2: 
            l.append('yi')
            l.append(d[10])
        elif ten > 2 : 
            l.append(d[ten])
            l.append(d[10])
    if N>10 and dec == 1:
        l.append('et')
        return ' '.join(l)
    elif dec > 0 :l.append(d[dec])
    return ' '.join(l)

exec(input().strip())
