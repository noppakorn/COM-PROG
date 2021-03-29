def row_number(t, e): # return row number of t containing e (top row is row #0)
    for i in range(len(t)) :
        if e in t[i] : return i

def flatten(t): # return a list of ints converted from list of lists of ints t
    return [j for i in t for j in i if j != 0]

def inversions(x): # return the number of inversions of list x
    c = 0
    for i in range(len(x)-1):
        for j in range(i+1,len(x)) :
            if x[i] > x[j] : c += 1
    return c

def solvable(t): # return True if tiling t (list of lists of ints) is solvable # otherwise return False
    if len(t)%2 == 1 and inversions(flatten(t))%2==0 : return True
    elif len(t)%2 == 0 :
        if inversions(flatten(t))%2==0 and row_number(t,0)%2 == 1: return True
        elif inversions(flatten(t))%2==1 and row_number(t,0)%2 == 0: return True
        return False
    return False

exec(input().strip())