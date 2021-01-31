[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11] = list(map(int,list(str(input()))))
n12 = (11-(13*n0+12*n1+11*n2+10*n3+9*n4+8*n5+7*n6+6*n7+5*n8+4*n9+3*n10+2*n11) % 11) % 10
print(str(n0),str(n1)+str(n2)+str(n3)+str(n4),str(n5)+str(n6)+str(n7)+str(n8)+str(n9),str(n10)+str(n11),n12)