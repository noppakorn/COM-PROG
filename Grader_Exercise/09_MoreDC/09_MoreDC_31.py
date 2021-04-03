def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a
def is_coprime(a, b, c):
    if gcd(a,b) == 1: return True
    if gcd(a,c) == 1: return True
    if gcd(c,b) == 1: return True
    return False
def primitive_Pythagorean_triples(max_len):
 # คืนลิสต์ ทภี่ ายในเกบ็ ลสิตย์ อ่ ยทมี่ สี มาชกิสามคา่ ของ a, b และ c
 # โดยที่ a  b  c  max_len
 # ลิสต์ย่อยต่าง ๆ ถูกจัดเรียงตามค่า c จากน้อยไปมาก
 # หากมีค่า c เท่ากัน ให้เรียงตามค่า a เชน่ ถา้ max_len = 65 จะได้
 # [[3, 4, 5], [5, 12, 13], [8, 15, 17], [7, 24, 25],
 # [20, 21, 29], [12, 35, 37], [9, 40, 41], [28, 45, 53],
 # [11, 60, 61], [16, 63, 65], [33, 56, 65]]
    triple = []
    i = 0
    while True:
        m,n = 2*i+3,2*i+1
        if is_coprime(m,n):
            a = m*n
            b = (m**2-n**2)//2
            c = (m**2+n**2)//2
            if a**2 + b**2 == c**2: triple.append([a,b,c])
            if c>max_len: break
        i += 1
print(primitive_Pythagorean_triples(65))
#exec(input().strip())