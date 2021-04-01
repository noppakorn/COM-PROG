R,C = int(input()),int(input())
for i in range(2,R+1):
    for j in range(1,C+1) :
        out = str(i*j)
        print(' '*(len(str(R*C))-len(out)) + out + ' ',end='')
    print()