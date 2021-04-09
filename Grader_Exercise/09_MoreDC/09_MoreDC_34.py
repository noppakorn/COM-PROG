def pattern1(nrows, ncols):
    return [[j for j in range(i*ncols+1,(i+1)*ncols+1)] for i in range(nrows)]
        
def pattern2(nrows, ncols):
    return [[j for j in range(3*i*ncols+1,3*(i+1)*ncols+1,3)] for i in range(nrows)]

def pattern3( N ):
    start = 0
    l = []
    for i in range(N):
        row = [j for j in range(start+1,start+1+N-i)]
        start = row[-1]
        if len(row) < N :
            row = [0]*(N-len(row)) + row
        l.append(row)
    return l
    
def pattern4( N ):
    pass

def pattern5( N ):
    pass

def pattern6( N ):
    pass

exec(input().strip()) 