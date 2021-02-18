x = input().split()
gt = ['F','D','D+','C','C+','B','B+','A']
ids,grades = [],[]
while x != ['q'] :
    ids.append(x[0])
    grades.append(x[1])
    x = input().split()
uids = input().split()
for i in uids : grades[ids.index(i)] = gt[min(7,gt.index(grades[ids.index(i)])+1)]
l = []
for i in range(len(ids)) : l.append([ids[i],grades[i]])
for i in sorted(l) :
    print(' '.join(i))