data = read_data('TH_COVID_EN.csv')
l = ['2021-04-%02d' % i for i in range(1,17)]
with open('max_new_cases_province.py','w+') as f:
    for i in range(len(l))  : 
        for j in range(i,len(l)) :
            exec("result = max_new_cases_province(data,'%s','%s')" % (l[i],l[j]))
            f.write("    \"assert max_new_cases_province(data,'%s','%s') == %s\",\n" % (l[i],l[j],result))