def factor(N):
    ans,k,c,l = N,2,0,[]
    while True:
        if ans%k == 0 : 
            ans /= k
            c += 1
        else : 
            if c != 0: l.append([k,c])
            k += 1
            c = 0
        if ans == 1 : 
            if c != 0: l.append([k,c])
            break
    return l
exec(input().strip())