nani,nina = {},{}
for i in range(int(input())) :
    x = input().split()
    nani[x[0]] = x[1]
    nina[x[1]] = x[0]
for i in range(int(input())) :
    y = input()
    if y in nani : print(nani[y])
    elif y in nina : print(nina[y])
    else : print('Not found')