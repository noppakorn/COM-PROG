uin = str(input())[1:-1].split(', ')
u = [float(i) for i in uin]
vin = str(input())[1:-1].split(', ')
v = [float(i) for i in vin]
print(u,'+',v,'=',[u[0]+v[0],u[1]+v[1],u[2]+v[2]])
