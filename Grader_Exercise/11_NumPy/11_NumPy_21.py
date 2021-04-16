import numpy as np

def sum_2_rows( M ):
    return M[::2,:] + M[1::2,:]

def sum_left_right( M ):
    return M[:,:M.shape[1]//2] + M[:,M.shape[1]//2:]

def sum_upper_lower( M ):
    return M[:M.shape[0]//2,:] + M[M.shape[0]//2:,:]

def sum_4_quadrants( M ):
    q00 = M[:M.shape[0]//2,:M.shape[1]//2]
    q01 = M[M.shape[0]//2:,:M.shape[1]//2]
    q10 = M[:M.shape[0]//2,M.shape[1]//2:]
    q11 = M[M.shape[0]//2:,M.shape[1]//2:]
    return np.sum(np.array([q00,q01,q10,q11]),axis=0)

def sum_4_cells( M ):
    return M[::2,::2]+ M[::2,1::2]+ M[1::2,::2]+ M[1::2,1::2]
    
def count_leap_years( years ):
    cy = years-543
    return cy[((cy % 4 == 0) & (cy % 100 != 0)) | ((cy % 4 == 0) & (cy % 100 == 0) & (cy % 400 == 0))].shape[0]

exec(input().strip())