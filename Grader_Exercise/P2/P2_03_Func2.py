def convex_polygon_area(p):
    sp = p
    suu = 0
    for i in range(0,len(sp)):
        if i == len(sp) -1 :
            suu += sp[i][0] * sp[0][1]
        else :
            suu += sp[i][0] * sp[i+1][1]
    for i in range(0,len(sp)):
        if i == len(sp) -1 :
            suu -= sp[i][1] * sp[0][0]
        else :
            suu -= sp[i][1] * sp[i+1][0]
    return abs(suu)/2
        
def is_heterogram(s):
    ls = [i for i in s.lower() if i.isalnum()]
    return len(set(ls)) == len(ls)

def replace_ignorecase(s, a, b):
    news = ''
    i = 0
    while i < len(s):
        window = s[i:i+len(a)]
        if a.lower() == window.lower():
            news += b
            i += len(a)
        else :
            news += s[i]
            i += 1
    return news
            
def top3(votes):
    return [i[1] for i in sorted([(-score,name) for name,score in votes.items()])[:3]]

x = [[2,1],[3,0],[5,1],[5,3],[3,5],[2,3]]
for k in range(2):
    exec(input().strip())