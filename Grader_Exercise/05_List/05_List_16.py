n = int(input())
l = []
while n != 1:
    l.append(n)
    if n%2 == 0: n = n // 2
    else: n = 3*n + 1
l.append(n)
print('->'.join([str(i) for i in l[-15:]]))