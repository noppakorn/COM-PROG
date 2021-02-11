import math

n = int(input())
print(math.sqrt(2*math.pi)*(n**(n+0.5))*(math.e**(-n+(1/(12*n+1)))))
print(math.sqrt(2*math.pi)*(n**(n+0.5))*(math.e**(-n+(1/(12*n)))))
