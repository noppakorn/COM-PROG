ticket = []
timein = []
timeor = []
queue = []

for i in range(int(input())) :
    x = input().split()
    if x[0] == 'reset' : 
        ticket.append(int(x[1]))
    elif x[0] == 'new' :
        print('ticket',ticket[-1])
        queue.append(ticket[-1])
        timein.append(int(x[1]))
        ticket.append(ticket[-1]+1)
    elif x[0] == 'next' : 
        od = queue[0]
        print('call',od)
        queue.pop(0)
        timeor.append(0)
    elif x[0] == 'order' :
        index = ticket.index(od)
        timeor[index] = int(x[1])
        print('qtime',od,timeor[index]-timein[index])
    elif x[0] == 'avg_qtime' :
        su,c = 0,0
        for i in range(len(timeor)) :
            if timeor[i] > timein[i] :
                su += timeor[i]-timein[i]
                c += 1
        print('avg_qtime',round(su/c,4))