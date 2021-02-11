import math

a = float(input())
b = float(input())
c = float(input())
print(round((-b-math.sqrt(b**2-(4*a*c)))/(2*a),3),round((-b+math.sqrt(b**2-(4*a*c)))/(2*a),3))
