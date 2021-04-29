import numpy as np

def replace(D, old_v, new_v):
    D[D == old_v] = new_v

def number_of_zero_rows( M ):
    return np.sum(np.all(M==0,axis=1))

exec(input().strip())