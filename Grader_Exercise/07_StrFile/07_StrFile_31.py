def checkDNA(dna):
    code = ['A','T','C','G']
    for i in dna : 
        if i not in code : return False
    return True

def R(dna) :
    code = ['A','T','C','G']
    coderev = ['T','A','G','C'] 
    outDNA = ''
    for i in dna : outDNA += coderev[code.index(i)]
    return outDNA[::-1]

def F(dna) :
    code = ['A','T','G','C']
    c = [0]*4
    for i in dna : c[code.index(i)] += 1
    return ('A=%d, T=%d, G=%d, C=%d') % tuple(c)

def D(dna,pattern) :
    c = 0
    for i in range(len(dna)-1) :
        if dna[i:i+2] == pattern : c += 1
    return c
    
dna,mode = input().strip().upper(),input().strip()
if checkDNA(dna) :
    if mode == 'R' : print(R(dna))
    elif mode == 'F' : print(F(dna))
    elif mode == 'D' : print(D(dna,input().strip()))
else : print('Invalid DNA')