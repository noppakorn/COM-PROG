h = int(input())
for i in range(h) :
    if i == h-1 : print('*'*(2*h-1))
    elif i == 0 :
        l = [' ']*(2*h-1)
        l[(2*h-1)//2] = '*'
        print(''.join(l))
    else :
        l = [' ']*(2*h-1)
        l[(2*h-1)//2 - i] = '*'
        l[(2*h-1)//2 + i] = '*'
        print(''.join(l))