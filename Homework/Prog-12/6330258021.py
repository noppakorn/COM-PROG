# Prog-12: COVID-19: The Latest Wave
# 6330258021 Noppakorn Jiravaranun

import numpy as np

def read_data(filename):
    d = np.loadtxt(filename, delimiter=",", encoding='utf-8', dtype=str)
    new_cases = np.array(d[1:,1:], dtype=int)
    norm = new_cases / np.max(new_cases, axis=1).reshape((new_cases.shape[0],1))
    return {'new_cases': new_cases,
    'norm_data': norm,
    'province_names': d[1:,0],
    'dates': d[0,1:]}

def max_new_cases_date(data):
    pass

def max_new_cases_province(data, beg_date, end_date):
    pass

def max_new_cases_province_by_dates(data):
    pass

def most_similar(data, province):
    pass

def most_similar_province_pair(data):
    pass

def most_similar_in_period(data, province, beg_date, end_date):
    pass

def main():
    
    return
main()