l = []
while True :
    i = input()
    if i != 'q' : 
        l.append(float(i))
    else : break
if len(l) == 0 : print('No Data')
else : print(round(sum(l)/len(l),2))