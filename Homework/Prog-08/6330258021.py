# Prog-08: Bag-of-words
# 6330258021 Noppakorn Jiravaranun

def readlines(fn) :
    fin = open(fn,'r')
    lines,line = [],fin.readline().strip()
    while line != '' :
        lines.append(line)
        line = fin.readline().strip()        
    fin.close()
    return lines

def getstopl(fn) :
    l = []
    for i in readlines(fn) : l += i.split()
    return l

def countandwords(lines) :
    cc,ca,s = 0,0,''
    for line in lines : 
        cc += len(line)
        for c in line :
            if c.isalnum() : 
                s += c
                ca += 1
            else : s += ' '
    return cc,ca,s.split()

def fhash(w,m) :
    h = 0
    for i in range(len(w)) : h += ord(w[i])*(37**i)
    return h % m

def getinfo(fn) :
    lines = readlines(fn)
    cc,ca,s = countandwords(lines)
    print('char count = %d' % cc) 
    print('alphanumeric count = %d' % ca)
    print('line count = %d' % len(lines))
    print('word count = %d' % len(s))
    return s

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
    bow = []
    for i in range(len(uwords)) :
        bow.append([uwords[i],cwords[i]])
    print('BoW = %s' % sorted(bow))

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
    bow = []
    for i in range(len(uwords)) :
        bow.append([uwords[i],cwords[i]])
    print('BoW = %s' % sorted(bow))