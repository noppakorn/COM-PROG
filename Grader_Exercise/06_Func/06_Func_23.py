def make_int_list(x):
    return [int(i) for i in x.split()]

def is_odd(e):
    return e % 2 == 1

def odd_list(alist):
    l = []
    for i in alist:
        if is_odd(i) : l.append(i)
    return l

def sum_square(alist):
    c = 0
    for i in alist:
        c += i**2
    return c

exec(input().strip())