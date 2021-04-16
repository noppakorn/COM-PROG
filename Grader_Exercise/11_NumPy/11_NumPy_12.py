import numpy as np

def toCelsius(f): return 5*(f-32)/9

def BMI(wh): return wh[:,0] / (wh[:,1]/100)**2

def distanceTo(p,Points): return np.sqrt((p[0] - Points[:,0])**2 + (p[1] - Points[:,1])**2)

exec(input().strip())