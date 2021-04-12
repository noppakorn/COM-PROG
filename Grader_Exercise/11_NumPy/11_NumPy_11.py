import numpy as np
# A is a 2-d array

def get_column_from_bottom_to_top( A, c ):
    return A[:,c,][::-1]
    
def get_odd_rows( A ):
    return A[np.arange(1,len(A),2)]
    
def get_even_column_last_row( A ):
    return A[-1,::2]
def get_diagonal1( A ): # A is a square matrix
 # from top-left corner down to bottom-right corner
    return np.array([A[i,i] for i in range(len(A))])
    
def get_diagonal2( A ): # A is a square matrix
 # from top-right corner down to bottom-left corner
    return np.array([A[i,-i-1] for i in range(len(A))])
    
exec(input().strip())