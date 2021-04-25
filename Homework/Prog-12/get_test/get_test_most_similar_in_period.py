data = read_data('TH_COVID_EN.csv')
import pandas as pd
l = ['2021-04-%02d' % i for i in range(1,17)]
ccc = pd.read_csv('TH_COVID_EN.csv')
with open('most_similar_in_period.py','w+') as f:
    for k in ccc['provinces']  : 
        for i in range(len(l))  : 
            for j in range(i,len(l)) :
                exec("result = most_similar_in_period(data,'%s','%s','%s')" % (k,l[i],l[j]))
                f.write("    \"assert most_similar_in_period(data,'%s','%s','%s') == %s\",\n" % (k,l[i],l[j],result))