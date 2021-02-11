x = input()
l = [0]*len(x)
for i in range(len(x)) :
    if x[i] == '(' : l[i] = '['
    elif x[i] == ')' : l[i] = ']'
    elif x[i] == '[' : l[i] = '('
    elif x[i] == ']' : l[i] = ')'
    else : l[i] = x[i]
print(''.join(l))