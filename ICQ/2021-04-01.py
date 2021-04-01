data = []
data.append([[0,1,2],[0,1,2],[0,1,2],[0,1,2]])
data.append([[0,1,2] for k in range(4)])
data.append([[0,1,2]]*4)
data.append([[e for e in range(3)] for k in range(4)])
for i in range(len(data)):
    print(i,data)