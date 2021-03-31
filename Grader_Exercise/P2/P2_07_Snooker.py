d = {'R':1,'Y':2,'G':3,'W':4,'B':5,'P':6,'K':7,'X':0}
cR = 6
p1s,p2s = 0,0
while cR>0:
    x = input()
    if x[1] == 'X' : continue
    if x[1] == 'R': cR -= 1
    if x[0] == '1': p1s += d[x[1]]+d[x[2]]
    elif x[0] == '2': p2s += d[x[1]]+d[x[2]]
c2 = 6
while c2>0:
    x = input()
    if x[1] != 'X': c2-=1
    if x[0] == '1': p1s += d[x[1]]
    elif x[0] == '2': p2s += d[x[1]]
print(p1s,p2s)
if p1s == p2s: print('Tie')
elif p1s > p2s: print('Player 1 wins')
elif p1s < p2s: print('Player 2 wins')