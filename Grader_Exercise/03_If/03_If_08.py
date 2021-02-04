day,month,year = int(input()),int(input()),int(input())-543
dm = [31,28,31,30,31,30,31,31,30,31,30,31]
if year % 4 == 0 and year % 100 != 0 : dm[1] +=1
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0 : dm[1] +=1
print(sum(dm[:month-1])+day)