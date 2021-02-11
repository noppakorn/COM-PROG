line = int(input())
x,y = [0]*line,[0]*line
for i in range(line) :
    [x[i],y[i]] = [int(i) for i in input().split(' ')]
z = input()
if z == 'Zig-Zag' : 
    print(min(x[::2] + y[1::2]),max(y[::2] + x[1::2]))
elif z == 'Zag-Zig' : 
    print(min(x[1::2] + y[::2]),max(y[1::2] + x[::2]))