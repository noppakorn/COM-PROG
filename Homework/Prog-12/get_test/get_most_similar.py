data = read_data('TH_COVID_EN.csv')
import pandas as pd
ccc = pd.read_csv('TH_COVID_EN.csv')
with open('most_similar.py','w+') as f:
    for i in ccc['provinces']  : 
        exec("result = most_similar(data,'%s')" % (i,))
        f.write("    \"assert most_similar(data,'%s') == \'%s\'\",\n" % (i,result))