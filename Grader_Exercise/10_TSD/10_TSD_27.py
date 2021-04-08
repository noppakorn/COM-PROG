def knows(R,x,y):
    return y in R[x]

def is_celeb(R,x): # return True if a is celeb, otherwise return False
    # return False if x knows someone who is not him/herself
    # return False if there exists someone in R who don't know x
    # otherwise return True
    for key,i in R.items() :
        if x not in i and key != x: return False
    if len(R[x]) == 1 and x in R[x] : return True
    if len(R[x]) > 0 : return False
    return True

def find_celeb(R):
    # for each person x in the party
    # if x is celeb --> return x
    # if no celeb in the party --> return None
    for i in R : 
        if is_celeb(R,i) : return i 

def read_relations() :
    # build a dictionary R from inputs
    # whose structure is shown in the example
    R = dict()
    inp = input().split()
    while inp != ['q']:
        if inp[0] not in R : R[inp[0]] = {inp[0],inp[1]}
        else : R[inp[0]].add(inp[1])
        if inp[1] not in R : R[inp[1]] = {inp[1]} 
        inp = input().split()
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)
        
exec(input().strip()) # do not remove this line