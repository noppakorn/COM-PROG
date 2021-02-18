color = ['Red','Yellow','Pink','Green','Orange','Blue','Purple']
day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
for i in range(4) : 
    i = input()
    if i not in day : print('Invalid day')
    else : print(color[day.index(i)])