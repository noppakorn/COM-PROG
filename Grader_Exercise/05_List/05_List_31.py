s = input().split()
op = list(input().strip(' '))
for i in op :
    if i == 'C' :
        s = s[len(s)//2:]+s[:len(s)//2]
    elif i == 'S' :
        nl = [0]*len(s)
        nl[1::2] = s[len(s)//2:]
        nl[::2] = s[:len(s)//2]
        s = nl
print(' '.join(s))