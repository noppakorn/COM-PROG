d = {}
order = []
for i in range(int(input())):
    inp = [e.strip() for e in input().split(':')]
    order.append(inp[0])
    d[inp[0]] = set(inp[1].split(', '))
inp = input()
city = d[inp]
match = []
for i,j in d.items():
    if len(j.intersection(city)) > 0 and i != inp:
        match.append(i)
if len(match) == 0 : print('Not Found')
else :
   for i in order:
       if i in match : print(i)