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

def fhash(w,m) :
    h = 0
    for i in range(len(w)) : h += ord(w[i])*(37**i)
    return h % m

file_name = input('File name = ').strip()
mode = input('Use feature hashing ? (y,Y,n,N) ').strip().lower()
while mode != 'n' and mode != 'y' :
    print('Try again.')
    mode = input('Use feature hashing ? (y,Y,n,N) ').strip().lower()
if mode == 'y' : m = int(input('M = ').strip())
print('-------------------')
lines = readlines(file_name)
cc,ca,words = 0,0,''
for line in lines : 
    cc += len(line)
    for c in line :
        if c.isalnum() : 
            words += c
            ca += 1
        else : words += ' '
words,uwords,cwords,stopwords = words.split(),[],[],[]
for i in readlines('stopwords.txt') : stopwords += i.split()
for word in words :
    word = word.lower()
    if word in stopwords  : continue
    if mode == 'y' : word = fhash(word,m)
    if word not in uwords : 
        uwords.append(word)
        cwords.append(1)
    else : cwords[uwords.index(word)] += 1
bow = []
for i in range(len(uwords)) : bow.append([uwords[i],cwords[i]])
print('char count = %d' % cc) 
print('alphanumeric count = %d' % ca)
print('line count = %d' % len(lines))
print('word count = %d' % len(words))
print('BoW = %s' % sorted(bow))