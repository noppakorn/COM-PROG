words = ''
for c in input().upper() : 
    if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' : words += c
    elif c == ' ' : words += '-'
print(words)