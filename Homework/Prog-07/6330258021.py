# Prog-07: EAN-13 Barcode
# 6330258021 Noppakorn Jiravaranun 

import math
import matplotlib.pyplot as plt
#-------------------------------------------------
def show_barcode(digits, ean13_code):  
    x = [[int(e) for e in ean13_code]]      
    plt.axis('off')       
    plt.imshow(x, aspect='auto', cmap='binary')      
    plt.title(digits)
    plt.show()   
#-------------------------------------------------
def test1():
    digits = input('Enter a 13-digit number: ')  
    codes = encode_EAN13(digits)     
    if codes == '':        
        print(digits, 'is not an EAN-13 number.')
    else:
        decoded_digits = decode_EAN13(codes)
        if decoded_digits == digits:
            show_barcode(digits, codes)
        else:
            print('Error in decoding.')
#-------------------------------------------------
L_codes = ['0001101', '0011001', '0010011', '0111101', '0100011', \
           '0110001', '0101111', '0111011', '0110111', '0001011']
G_codes = ['0100111', '0110011', '0011011', '0100001', '0011101', \
           '0111001', '0000101', '0010001', '0001001', '0010111']
R_codes = ['1110010', '1100110', '1101100', '1000010', '1011100', \
           '1001110', '1010000', '1000100', '1001000', '1110100']

#=================================================




def codes_of(digits, patterns):
    pass


def digits_of(codes):
    pass


def patterns_of(codes):
    pass


def check_digit(digits):
    pass


def encode_EAN13(digits):
    pass


def decode_EAN13(codes):
    pass


#-------------------------------------------------
test1()
