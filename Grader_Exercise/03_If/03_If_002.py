d,m,y = input().split(' ')
d,m,y = int(d),int(m),int(y)-543
n = 31
if m == 2 :
    if y % 4 == 0 and y % 100 != 0 : n = 29
    elif y % 4 == 0 and y % 100 == 0 and y % 400 == 0 : n = 29
    else : n = 28
elif m in [4,6,9,11] : n = 30
elif m in [1,3,5,7,8,10,12] : n = 31

d += 15
if d > n :
    d -= n
    m += 1
if m > 12 :
    m -= 12
    y += 1

print(str(d)+'/'+str(m)+'/'+str(y+543))