l = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
g = ['0100111', '0110011', '0011011', '0100001', '0011101', '0111001', '0000101', '0010001', '0001001', '0010111']
r = ['1110010', '1100110', '1101100', '1000010', '1011100', '1001110', '1010000', '1000100', '1001000', '1110100']

def patterns_of(codes):
    s,nc = '',[]
    for i in range(len(codes)//7) : nc.append(codes[7*i:7*(i+1)])
    for i in nc :
        if i in l : s += 'L'
        elif i in g : s += 'G'
        elif i in r : s += 'R'
        else : return ''
    return s

print(patterns_of('01000110111001'))
print(patterns_of('01000111111111'))