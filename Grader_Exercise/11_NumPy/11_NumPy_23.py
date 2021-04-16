import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight,data):
    wdata = weight * data[:,1:]
    swdata = np.sum(wdata,axis=1)
    ltm = data[swdata<np.mean(swdata)][:,0]
    if ltm.shape[0] > 0:
        print(', '.join([str(i) for i in ltm]))
    else : print("None")

exec(input().strip())