import string
def remove_space(s) :
    out = []
    for i in s :
        if i in string.ascii_letters : out.append(i.lower())
    return sorted(out)

if remove_space(input()) == remove_space(input()) : print('YES')
else : print('NO')