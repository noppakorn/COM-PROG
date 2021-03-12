import string
s = ''
for i in list(input()) :
    if i not in string.punctuation : s+=i
    else : s += ' '
x = s.split()
print(x[0].lower(),end='')
for i in x[1:] : print(i.title(),end='')