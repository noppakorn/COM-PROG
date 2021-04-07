d1 = {i[0]:i[1] for i in [i.strip().split(',') for i in open(input()).readlines()]}
d2 = {i[0]:i[1] for i in [i.strip().split(',') for i in open(input()).readlines()]}
for i in [i.strip().split(',') for i in open(input()).readlines()] : 
    if i[0] in d1 and i[1] in d2 :
        print(d1[i[0]] + ',' + d2[i[1]])
    else :
        print('record error')