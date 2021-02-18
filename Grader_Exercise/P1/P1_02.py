mode = input()
if mode == 'str2RLE' :
    s = input()
    char = s[0]
    c = 0
    for i in s :
        if i == char : c += 1
        else :
            print(char,c)
            char = i
            c = 1
    print(char,c)
elif mode == 'RLE2str' :
    x = input().split()
    for i in range(len(x)//2) :
        print(x[2*i]*int(x[2*i+1]),end='')
else : print('Error')