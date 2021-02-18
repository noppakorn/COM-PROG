# Prog-05: The 24 Game
# 6330258021 Noppakorn Jiravaranun

from itertools import permutations, product
import math

def generate_all_combinations(num_list, operators):
    all_combi = []
    for n,o in product(sorted(set(permutations(num_list))),
                       product(operators, repeat=3)): 
        x = [None]*(len(n)+len(o))
        x[::2] = n
        x[1::2] = o
        all_combi.append(x)
    return all_combi
#--------------------------------------------------------- 
def calc(num1,op,num2) :
    if op == '+' : return num1+num2
    elif op == '-' : return num1-num2
    elif op == '*' : return num1*num2
    elif op == '/' and num2 != 0 : return num1/num2
    elif op == '/' and num2 == 0 : return float('nan')
#---------------------------------------------------------
nums = input('Enter 4 integers: ')
cases = generate_all_combinations( [int(i) for i in nums.split()],  '+-*/' )
w = False
for i in cases :
    if calc(calc(calc(i[0],i[1],i[2]),i[3],i[4]),i[5],i[6]) == 24 :
        print('(','(',i[0],i[1],i[2],')',i[3],i[4],')',i[5],i[6],'=',24)
        w = True
        break
    if calc(calc(i[0],i[1],calc(i[2],i[3],i[4])),i[5],i[6]) == 24 :
        print('(',i[0],i[1],'(',i[2],i[3],i[4],')',')',i[5],i[6],'=',24)                
        w = True
        break
    if calc(calc(i[0],i[1],i[2]),i[3],calc(i[4],i[5],i[6])) == 24 :
        print('(',i[0],i[1],i[2],')',i[3],'(',i[4],i[5],i[6],')','=',24)
        w = True
        break
    if calc(i[0],i[1],calc(calc(i[2],i[3],i[4]),i[5],i[6])) == 24 :
        print(i[0],i[1],'(','(',i[2],i[3],i[4],')',i[5],i[6],')','=',24)
        w = True
        break
    if calc(i[0],i[1],calc(i[2],i[3],calc(i[4],i[5],i[6]))) == 24 :
        print(i[0],i[1],'(',i[2],i[3],'(',i[4],i[5],i[6],')',')','=',24)
        w = True
        break
if not w : print('No Solutions')