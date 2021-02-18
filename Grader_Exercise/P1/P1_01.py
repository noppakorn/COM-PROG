i1,i2 = input().split(),input().split()
if int(i1[-1]) < int(i2[-1]) : print(i1[0])
elif int(i1[-1]) > int(i2[-1]) : print(i2[0])
else :
    if i1[1] == i2[1] :
        if i1[2] == i2[2] : print(i1[0],i2[0])
        elif int(i1[2].strip(',')) < int(i2[2].strip(',')) : print(i1[0])
        elif int(i1[2].strip(',')) > int(i2[2].strip(',')) : print(i2[0])
    else :
        for m in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] :
            if i1[1] == m :
                print(i1[0])
                break
            elif i2[1] == m :
                print(i2[0])
                break