m = int(input())

r,p1,p2 = 0,0,0
while True :
    if r == 3*m and p1 < m and p2 < m: 
        print(p1,p2)
        print('Tie')
        break 
    elif p1 == m and p2<p1 : 
        print(p1,p2)
        print('Player 1 wins')
        break
    elif p2 == m and p1<p2 : 
        print(p1,p2)
        print('Player 2 wins')
        break
    s = input().split()
    if s[0] == 'R' :
        if s[1] == 'S' : p1 += 1
        elif s[1] == 'P' : p2 += 1
    elif s[0] == 'P' :
        if s[1] == 'R' : p1 += 1
        elif s[1] == 'S' : p2 += 1
    elif s[0] == 'S' :
        if s[1] == 'P' : p1 += 1
        elif s[1] == 'R' : p2 += 1
    r+=1
