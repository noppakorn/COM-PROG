first = ['Robert','William','James','John','Margaret','Edward','Sarah','Andrew','Anthony','Deborah']
nick = ['Dick','Bill','Jim','Jack','Peggy','Ed','Sally','Andy','Tony','Debbie']
for i in range(int(input())) : 
    name = input()
    if name in first : print(nick[first.index(name)])
    elif name in nick : print(first[nick.index(name)])
    else : print('Not found')