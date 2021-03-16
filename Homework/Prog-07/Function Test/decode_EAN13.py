L_codes = ['0001101', '0011001', '0010011', '0111101', '0100011', \
           '0110001', '0101111', '0111011', '0110111', '0001011']
G_codes = ['0100111', '0110011', '0011011', '0100001', '0011101', \
           '0111001', '0000101', '0010001', '0001001', '0010111']
R_codes = ['1110010', '1100110', '1101100', '1000010', '1011100', \
           '1001110', '1010000', '1000100', '1001000', '1110100']

#=================================================
enct = ['LLLLLL', 'LLGLGG', 'LLGGLG', 'LLGGGL', 'LGLLGG', 'LGGLLG', 'LGGGLL', 'LGLGLG', 'LGLGGL', 'LGGLGL']

def codes_of(digits, patterns):
    s = ''
    for i in range(len(digits)) :
        if patterns[i] == 'L' : s += L_codes[int(digits[i])]
        elif patterns[i] == 'G' : s += G_codes[int(digits[i])]
        elif patterns[i] == 'R' : s += R_codes[int(digits[i])]
    return s

def digits_of(codes):
    s,nc = '',[]
    for i in range(len(codes)//7) : nc.append(codes[7*i:7*(i+1)])
    for i in nc :
        if i in L_codes : s += str(L_codes.index(i))
        elif i in G_codes : s += str(G_codes.index(i))
        elif i in R_codes : s += str(R_codes.index(i))
        else : return ''
    return s

def patterns_of(codes):
    s,nc = '',[]
    for i in range(len(codes)//7) : nc.append(codes[7*i:7*(i+1)])
    for i in nc :
        if i in L_codes : s += 'L'
        elif i in G_codes : s += 'G'
        elif i in R_codes : s += 'R'
        else : return ''
    return s

def check_digit(digits):
    su,m,v = 0,10,[1,3]*6
    for i in range(len(digits)) : su += int(digits[i])*v[i]
    while m < su : m += 10
    return str(m - su)

def encode_EAN13(digits):
    if len(digits) != 13 : return ''
    for i in digits :
        if i not in '1234567890' : return ''
    if check_digit(digits[:-1]) != digits[-1] : return ''
    return '101' + codes_of(digits[1:7],enct[int(digits[0])]) + '01010' + codes_of(digits[7:],'RRRRRR') + '101'

def decode_EAN13(codes):
    if len(codes) != 95 or codes[:3] != '101' or codes[-3:] != '101' or codes[45:50] != '01010': return ''
    g1,g2 = codes[3:45],codes[50:-3]
    if patterns_of(g1[::-1]) == 'RRRRRR' : g1,g2 = g2[::-1],g1[::-1]
    digits =  digits_of(g1) + digits_of(g2)
    if len(digits) != 12 : return ''
    digits = str(enct.index(patterns_of(g1))) + digits
    if check_digit(digits[:-1]) != digits[-1] : return ''
    return digits


#print(patterns_of('0010011'[::-1]))
#c = '10100100110011001010011100110110010111001001101010111001010111001001110110011011101001101100101'
#print(decode_EAN13(c))
#print('3210292045192')
#c = '10111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111101'
#print(decode_EAN13(c))
c = '10100100110011001010011100110110010111001001101010111001010111001001110110011011101001101100101'
print(decode_EAN13(c[::-1]))