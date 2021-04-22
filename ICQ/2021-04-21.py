import numpy as np
x = [1,2,3]
y = [4,5,6]
z = x+y
z = np.array(z) + np.array(x*2)
print(z)