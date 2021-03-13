import string
def no_lowercase(t):
    for i in t : 
        if i in string.ascii_lowercase : return False
    return True
def no_uppercase(t):
    for i in t : 
        if i in string.ascii_uppercase : return False
    return True
def no_number(t):
    for i in t : 
        if i in string.digits : return False
    return True
def no_symbol(t):
    for i in t : 
        if i in string.punctuation : return False
    return True
def character_repetition(t):
    for i in range(len(t)-3) :
        l = []
        for j in t[i:i+4] :
            if j not in l : l.append(j)
        if len(l) == 1 : return True
    return False
def number_sequence(t):
    nsq = '01234567890'
    for i in range(len(t)-3) :
        if t[i:i+4] in nsq or t[i:i+4] in nsq[::-1] : return True
    return False 
def letter_sequence(t):
    t = t.lower()
    lsq = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(t)-3) :
        if t[i:i+4] in lsq or t[i:i+4] in lsq[::-1] : return True
    return False 
def keyboard_pattern(t):
    t = t.lower()
    r0,r1,r2,r3 = '!@#$%^&*()_+','qwertyuiop','asdfghjkl','zxcvbnm'
    for i in range(len(t)-3) :
        if t[i:i+4] in r0 or t[i:i+4] in r0[::-1] : return True
        elif t[i:i+4] in r1 or t[i:i+4] in r1[::-1] : return True
        elif t[i:i+4] in r2 or t[i:i+4] in r2[::-1] : return True
        elif t[i:i+4] in r3 or t[i:i+4] in r3[::-1] : return True
    return False
#-----------------------------
passw = input().strip()
errors = []
if len(passw) < 8: errors.append("Less than 8 characters")
if no_lowercase(passw): errors.append("No lowercase letters")
if no_uppercase(passw): errors.append("No uppercase letters")
if no_number(passw) : errors.append('No numbers')
if no_symbol(passw) : errors.append('No symbols')
if character_repetition(passw) : errors.append('Character repetition')
if number_sequence(passw) : errors.append('Number sequence')
if letter_sequence(passw) : errors.append('Letter sequence')
if keyboard_pattern(passw) : errors.append('Keyboard pattern')
if len(errors) == 0: errors.append('OK')
for i in errors : print(i)