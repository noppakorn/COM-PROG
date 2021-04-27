class Complex :
    def __init__(self,a,b):
        self.re = a
        self.im = b
    def __str__(self):
        if self.re == 0 and self.im == 0:
            return '0'
        s = ''
        if self.re > 0 or self.re < 0:
            s += str(self.re)
            if self.im > 0 :
                s += '+'
        if self.im == -1:
            s += '-i'
        elif self.im != 0 :
            if self.im != 1 :
                s += str(self.im)
            s += 'i'
        return s
    def __add__(self, rhs):
        re = self.re + rhs.re
        im = self.im + rhs.im 
        return Complex(re,im) 
    def __mul__(self, rhs):
        re = (self.re*rhs.re) - (self.im*rhs.im)
        im = (self.re*rhs.im) + (self.im*rhs.re)
        return Complex(re,im) 
    def __truediv__(self, rhs):
        re = ((self.re*rhs.re) + (self.im*rhs.im)) / (rhs.im**2+rhs.re**2)
        im = ((-self.re*rhs.im) + (self.im*rhs.re)) / (rhs.im**2+rhs.re**2)
        return Complex(re,im)
t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)