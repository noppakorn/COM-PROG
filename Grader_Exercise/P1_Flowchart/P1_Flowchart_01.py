x1,x2,x3,x4,x5 = [int(e) for e in input().split()] 
if x1-x5>x2 :
    if x2>x3+x1 :
        if x3+x5>x4 : 
            print("C5")
            exit(0)
        elif x3 < x5 : print("C6")
        else : print("C7")
        print("C8")
else :
    if x2-x1 > x3 : exit(0)
    elif x4<x5+x1 :
        if x3+x2>x5 : print("C3")
        else : print("C2")
        print("C4")
    else : print("C1")