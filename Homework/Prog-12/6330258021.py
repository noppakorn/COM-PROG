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
    su = np.sum(data['new_cases'],axis=0)
    return (data['dates'][np.argmax(su)],np.max(su))

def max_new_cases_province(data, beg_date, end_date):
    sum_by_prov = np.sum(data['new_cases'][:,np.argmax(data['dates'] == beg_date):np.argmax(data['dates'] == end_date)+1],axis=1)
    return (data['province_names'][np.argmax(sum_by_prov)],np.max(sum_by_prov))

def max_new_cases_province_by_dates(data):
    return np.array([data['dates'],data['province_names'][np.argmax(data['new_cases'],axis=0)],np.max(data['new_cases'],axis=0)]).T

def most_similar(data, province):
    sig_sq = np.sum((data['norm_data'] - data['norm_data'][data['province_names'] == province])**2,axis=1)
    return data['province_names'][data['province_names'] != province][np.argmin(sig_sq[sig_sq != 0])]

def most_similar_province_pair(data):

    pass

def most_similar_in_period(data, province, beg_date, end_date):
    dates = data['dates']
    dr = dates[np.argmax(dates == beg_date):np.argmax(dates == end_date)+1]
    wr = np.arange(0,dates.shape[0]-dr.shape[0]+1)
    windows = np.arange(0,dr.shape[0]) + wr.reshape(wr.shape[0],1)
    sdata = data['norm_data'][:,windows]
    ndata_prov = data['new_cases'][data['province_names'] == province][:,np.argmax(dates == beg_date):np.argmax(dates == end_date)+1]
    print(ndata_prov)
    sum_sq_by_dr = np.sum((sdata - ndata_prov)**2,axis=1)
    print(sdata.shape)
    print(ndata_prov.shape)
    print(sum_sq_by_dr)
    return 'Fin'
    

def main():
    #data = read_data('TH_20210401_20210416.csv')
    data = read_data('sample.csv')
    #print(max_new_cases_date(data))
    #print(max_new_cases_province(data, '2021-04-10', '2021-04-13'))
    #print(max_new_cases_province_by_dates(data))
    #print(most_similar(data, 'กรุงเทพมหานคร'))
    #print(most_similar_province_pair(data))
    print(most_similar_in_period(data, 'กรุงเทพมหานคร', '2021-04-15', '2021-04-16' ))
    #print(most_similar_in_period(data, 'กรุงเทพมหานคร', '2021-04-05', '2021-04-09' ))
    #print(most_similar_in_period(data, 'กรุงเทพมหานคร', '2021-04-01', '2021-04-16' ))
    return
main()