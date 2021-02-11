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