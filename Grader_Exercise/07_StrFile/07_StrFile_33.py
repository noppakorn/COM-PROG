fn = input().split()
form = [[i[0][-2:],i[0],i[1]] for i in [i.strip().split() for i in open(fn[0])]] + [[i[0][-2:],i[0],i[1]] for i in [i.strip().split() for i in open(fn[1])]]
for i in sorted(form): print(i[1],i[2])
