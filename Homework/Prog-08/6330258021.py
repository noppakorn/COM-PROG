# Prog-08: Bag-of-words
# 6330258021 Noppakorn Jiravaranun

file_name = input('File name = ').strip()
mode = input('Use feature hashing ? (y,Y,n,N) ').strip().lower()

if mode == 'y' : 
    m = input('M = ').strip()
    print('-------------------')
    print(m)


elif mode == 'n' :
    print('-------------------')

else : 
    print('Try again')