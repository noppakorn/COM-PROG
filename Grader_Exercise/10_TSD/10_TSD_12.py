sc = int(input())-1
if sc < 0 :
    print(0)
    print(0) 
else :
    x = set(int(e) for e in input().split())
    union = x.copy() 
    intersect = x.copy()
    for i in range(sc):
        x = set(int(e) for e in input().split())
        union = union.union(x)
        intersect = intersect.intersection(x)
    print(len(union))
    print(len(intersect))