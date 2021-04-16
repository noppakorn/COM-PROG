import numpy as np
def p( X ):
    logitx = -3.98 + X[:,0]*0.1 + X[:,1]*0.5
    return 1/(1+np.e**-logitx)

exec(input().strip())