def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m

def mult_c(c, A): return [[j*c for j in i] for i in A]

def mult(A, B):
    l = []
    for Ai in A:
        sl = []
        for x in range(len(B[0])) :
            Bj = [i[x] for i in B]
            sl.append(sum([Ai[e]*Bj[e] for e in range(len(Ai))]))
        l.append(sl)
    return l
exec(input().strip())