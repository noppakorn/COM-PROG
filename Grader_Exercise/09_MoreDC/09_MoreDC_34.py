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
    l = []
    start = 0
    for i in range(N):
        row = []
        c = 0
        while c < N - i :
            start += 1 + c + i
            row.append(start)
            c += 1
        if len(row) < N :
            row = [0]*(N-len(row)) + row
        l.append(row)
        start = row[i] - 1
    return l
            
def pattern5( N ):
    l = []
    start = 1
    for i in range(N):
        row = []
        c = 0
        while c < N - i :
            row.append(start)
            start += N - c
            c += 1
        if len(row) < N :
                row = [0]*(N-len(row)) + row
        l.append(row)
        start = row[i] + 1
    return l

def pattern6( N ):
    l = [[0]*N for i in range(N)]
    c = 0
    for j in l:
        for k in range(c,N):
            ele = c + 1
            j[k]= 
        c += 1
    return l


print(pattern6(5))
#exec(input().strip()) 