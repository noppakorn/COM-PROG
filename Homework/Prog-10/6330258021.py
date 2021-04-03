# Prog-10: Steganography
# 6330258021 Noppakorn Jiravaranun

import math
import copy
import numpy
from PIL import Image

# -----------------------------------------
def load_image(filename):  
    im = Image.open(filename).convert('RGB')      
    return numpy.asarray(im).tolist()       
      
def save_image(img, filename):
    im = Image.fromarray(numpy.uint8(img))   
    im.save(filename)
  
def show_image(filename):     
    im = Image.open(filename)        
    im.show()

def clone_image(img):
    return copy.deepcopy(img)

def char_to_bits(ch):
    return ('0000000' + bin(ord(ch))[2:])[-8:]

def bits_to_char( bits ):
    return chr( bits_to_int(bits) )

def int_to_bits(n):
    return ('0'*16 + bin(n)[2:])[-16:]

def bits_to_int( bits ):
    return int(bits,2)

def main():
    op = input('E(mbed text) or G(et text): ')
    if op == 'E' or op == 'G':
        file_in = input('Input image file (.png): ')
        if file_in[-4:] != '.png':
            file_in = file_in + '.png'
        if op == 'E':
            text = input('Text to be embedded: ')
            file_out = file_in[:-4] + '_x' + '.png'
            success = embed_text_to_image(text, file_in, file_out)
            if success:
                print('The output image file is', file_out)
            else:
                print('Need a bigger image.')
        else:
            txt = get_embedded_text_from_image(file_in)
            if txt == '':
                print('No hidden text.')
            else:
                print('The hidden text is', txt)
    else:
        print('Try again, re-enter E or G')
# --------------------------------------------------
def convert(C,b):
    if C%2 == 0: 
        if b == 0: return C
        else : return C+1
    elif C%2 == 1:
        if b == 0: return C-1
        else : return C
# --------------------------------------------------
def embed_text_to_image(text, file_in, file_out):
    t2be = SPECIAL_BITS + int_to_bits(len(text)) + ''.join([char_to_bits(i) for i in text]) + SPECIAL_BITS
    img = load_image(file_in)
    imgcf = [k for i in clone_image(img) for j in i for k in j]
    if len(imgcf) < len(t2be) : return False
    for e in range(len(t2be)) : imgcf[e] = convert(int(imgcf[e]),int(t2be[e]))
    imgoutpix = [[imgcf[i],imgcf[i+1],imgcf[i+2]] for i in range(0,len(imgcf),3)]
    save_image([imgoutpix[e*len(img[0]):(e+1)*len(img[0])] for e in range(0,len(img))],file_out)
    if get_embedded_text_from_image(file_out) == text : return True
# --------------------------------------------------
def get_embedded_text_from_image(file_in):
    img = load_image(file_in)
    imgcf = [k for i in clone_image(img) for j in i for k in j]
    if ''.join([str(i%2) for i in imgcf[:16]]) == SPECIAL_BITS : 
        cc = bits_to_int(''.join([str(i%2) for i in imgcf[16:32]]))
        if ''.join([str(i%2) for i in imgcf[32+(8*cc):32+(8*cc)+16]]) == SPECIAL_BITS : return ''.join([bits_to_char(''.join([str(j%2) for j in imgcf[32+i:32+i+8]])) for i in range(0,cc*8,8)])
    return '' 
# --------------------------------------------------
SPECIAL_BITS = '0100111101001011'
main()