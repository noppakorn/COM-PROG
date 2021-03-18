# Prog-08: Bag-of-words
# 6330258021 Noppakorn Jiravaranun

def readlines(fn) :
    fin = open(fn,'r')
    lines,line = [],fin.readline().strip()
    while len(line) != 0 :
        lines.append(line.strip())
        line = fin.readline()        
    fin.close()
    return lines

def getstopl(fn) :
    l = []
    for i in readlines(fn) : l += i.split()
    return l

def fhash(w,m) :
    h = 0
    for i in range(len(w)) : h += ord(w[i])*(37**i)
    return h % m

def getinfo(fn) :
    lines = readlines(fn)
    cc,ca,s = 0,0,''
    for line in lines : 
        cc += len(line)
        for c in line :
            if c.isalnum() : 
                s += c
                ca += 1
            else : s += ' '
    s = s.split()
    print('char count = %d' % cc) 
    print('alphanumeric count = %d' % ca)
    print('line count = %d' % len(lines))
    print('word count = %d' % len(s))
    return s

def print_bow(uword,cword) :
    bow = []
    for i in range(len(uwords)) : bow.append([uwords[i],cwords[i]])
    print('BoW = %s' % sorted(bow))

file_name = input('File name = ').strip()
mode = input('Use feature hashing ? (y,Y,n,N) ').strip().lower()
while mode != 'n' and mode != 'y' :
    print('Try again.')
    mode = input('Use feature hashing ? (y,Y,n,N) ').strip().lower()
print('-------------------')

if mode == 'n' :
    uwords,cwords = [],[]
    stopwords = getstopl('stopwords.txt')
    for word in getinfo(file_name) :
        word = word.lower()
        if word in stopwords  : continue
        elif word not in uwords : 
            uwords.append(word)
            cwords.append(1)
        else : cwords[uwords.index(word)] += 1
    print_bow(uwords,cwords)

elif mode == 'y' :
    m = int(input('M = ').strip())
    uwords,cwords = [],[]
    stopwords = getstopl('stopwords.txt')
    for word in getinfo(file_name) :
        word = word.lower()
        if word in stopwords  : continue
        hword = fhash(word,m)
        if hword not in uwords : 
            uwords.append(hword)
            cwords.append(1)
        else : cwords[uwords.index(hword)] += 1
    print_bow(uwords,cwords)