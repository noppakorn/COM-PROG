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
    triple = []
    for c in range(max_len+1):
        for b in range(c) :
            for a in range(b):
                if c**2 == a**2 + b**2 and is_coprime(a,b,c) : triple.append([c,a,b])
    return [[i[1],i[2],i[0]] for i in sorted(triple)]

exec(input().strip())