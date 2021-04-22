dept = {}
for i in range(int(input())) :
    iii = input().split()
    for j in iii : dept[iii[0]] = int(iii[1])
student = []
for i in range(int(input())):
    sd = input().split()
    student.append([float(sd[1]),sd[0],sd[2:]])
result = {}
for score,id,de in sorted(student)[::-1]:
    for i in de:
        if dept[i] > 0 :
            dept[i] -= 1
            result[id] = i
            break
for i,j in sorted(result.items()) : print(i,j)