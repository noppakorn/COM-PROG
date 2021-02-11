x = str(input())
o1 = x[3::7]
o2 = x[7::5]
o3 = int(o1) + int(o2) + 10000
o4 = str(o3)[-4:-1]
o5 = (int(o4[0])+int(o4[1])+int(o4[2])) % 10 + 1
o6 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'][o5-1]
print(o4+o6)
