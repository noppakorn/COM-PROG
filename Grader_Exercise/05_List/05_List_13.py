l= []
for i in range(int(input())) : l.append(input())
l += input().split()
i3 = input()
while i3 != '-1':
    l.append(i3)
    i3 = input()
out = []
for i in range(len(l)) :
    if i%2 == 0 : out.append(int(l[i]))
    else : out.insert(0,int(l[i]))
print(out)