x = input()
y = input()
if len(x) == len(y) :
    s = 0
    for i in range(len(y)):
        if x[i] == y[i] : s += 1
    print(s)
else : print('Incomplete answer')