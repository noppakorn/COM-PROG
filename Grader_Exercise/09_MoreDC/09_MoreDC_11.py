for x in range(int(input())) :
    i = input()
    c = 0
    for j in i:
        if j == '.' : c += 1
        else: break
    print(('.'*(c//2))+i[c:])