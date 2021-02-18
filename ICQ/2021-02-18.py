result = 0
s = "1 2 123 12 12 1"
for c in s :
    if c == "1" :
        result += 1
    if c == "12" :
        result += 3
print(result)

S = ""
for i in range(0,18,2) : 
    if i % 3 == 0 :
        S += str(i) + " "
print(S)
for i in range(1,6) : print(str(i) * i)