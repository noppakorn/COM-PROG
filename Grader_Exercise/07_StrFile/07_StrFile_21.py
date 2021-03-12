import string
def rot13(txt_in) :
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    out = ''
    for i in txt_in :
        if i in upper : out += upper[(upper.find(i)+13)%26]
        elif i in lower : out += lower[(lower.find(i)+13)%26]
        else : out += i
    return out
x = input()
while x != 'end' : 
    print(rot13(x))
    x = input()