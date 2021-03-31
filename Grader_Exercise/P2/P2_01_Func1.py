def is_odd(n): return n%2 == 1
def has_odds(x) :
    for i in x : 
        if i%2 == 1: return True
    return False
def all_odds(x):
    for i in x : 
        if i%2 == 0: return False
    return True
def no_odds(x):
    for i in x :
        if i%2 == 1: return False
    return True
def get_odds(x): return [i for i in x if i%2==1]
def zip_odds(a,b):
    oa,ob = get_odds(a),get_odds(b)
    for i in range(len(ob)):
        oa.insert(2*i+1,ob[i])
    return oa
exec(input().strip())